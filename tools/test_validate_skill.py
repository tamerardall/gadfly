import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_skill import validate  # noqa: E402

SCRIPT = Path(__file__).parent / "validate_skill.py"
STEMS = ["opposing-expert", "fact-checker", "skeptic", "newcomer", "veteran"]
TECH_STEMS = ["architecture-critic", "security", "scalability", "already-solved"]
EDGE = [
    "### Non-English draft",
    "### Draft too short",
    "### Draft file missing",
    "### Instructions inside the draft",
    "### Research found nothing",
    "### Input type unclear",
]
PLACEHOLDERS = ["{{title}}", "{{counts}}", "{{evidence_banner}}", "{{objections}}", "{{skipped_personas}}"]

SKILL_MD = (
    "---\nname: gadfly\ndescription: Use when you want a draft challenged.\n---\n\n"
    "# Gadfly\n\nPersonas: " + ", ".join(STEMS + TECH_STEMS) + "\n\n## Edge cases\n\n"
    + "\n\nhandled.\n\n".join(EDGE) + "\n\nhandled.\n"
)
PERSONA_MD = (
    "---\nname: {stem}\nrole: a reader\nhunts_for: weak spots\n---\n\n"
    "## Your angle\n\nx\n\n## What to return\n\ny\n"
)
TEMPLATE_MD = "\n".join(PLACEHOLDERS) + "\n"
RESEARCH_MD = "# Research agent\n\n## Output\n\nx\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_tree(tmp: Path) -> Path:
    write(tmp / "SKILL.md", SKILL_MD)
    for stem in STEMS:
        write(tmp / "personas" / "content" / f"{stem}.md", PERSONA_MD.format(stem=stem))
    for stem in TECH_STEMS:
        write(tmp / "personas" / "technical" / f"{stem}.md", PERSONA_MD.format(stem=stem))
    write(tmp / "report-template.md", TEMPLATE_MD)
    write(tmp / "research-agent.md", RESEARCH_MD)
    write(tmp / "research-agent-technical.md", RESEARCH_MD)
    write(tmp / "evals" / "quit-todo-apps.md", "draft\n")
    write(tmp / "evals" / "quit-todo-apps.expected.md", "expected\n")
    write(tmp / "evals" / "technical-idea.md", "draft\n")
    write(tmp / "evals" / "technical-idea.expected.md", "expected\n")
    return tmp


class ValidateSkillTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.addCleanup(self._td.cleanup)
        self.tmp = Path(self._td.name)
        self.root = make_tree(self.tmp)

    def errors_text(self):
        return "\n".join(validate(self.root))

    def edit(self, rel, old, new=""):
        p = self.root / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text)
        p.write_text(text.replace(old, new), encoding="utf-8")

    def test_minimal_valid_tree_has_no_errors(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_skill_md(self):
        (self.root / "SKILL.md").unlink()
        errs = validate(self.root)
        self.assertEqual(len([e for e in errs if "SKILL.md" in e]), len(errs))
        self.assertTrue(errs)

    def test_wrong_name_in_frontmatter(self):
        self.edit("SKILL.md", "name: gadfly", "name: other")
        self.assertIn("name", self.errors_text())

    def test_description_must_start_with_use_when(self):
        self.edit("SKILL.md", "Use when you want a draft challenged.", "Does things")
        self.assertIn("description", self.errors_text())

    def test_description_too_long(self):
        self.edit("SKILL.md", "challenged.", "x" * 1100)
        self.assertIn("description", self.errors_text())

    def test_persona_missing_frontmatter_key(self):
        self.edit("personas/content/skeptic.md", "hunts_for: weak spots\n")
        errs = [e for e in validate(self.root) if "skeptic" in e and "hunts_for" in e]
        self.assertEqual(len(errs), 1)

    def test_persona_missing_heading(self):
        self.edit("personas/content/newcomer.md", "## What to return\n")
        self.assertTrue([e for e in validate(self.root) if "newcomer" in e])

    def test_extra_persona_file_rejected(self):
        write(self.root / "personas" / "content" / "extra.md", "x")
        self.assertIn("extra", self.errors_text())

    def test_technical_persona_missing_file(self):
        (self.root / "personas" / "technical" / "security.md").unlink()
        self.assertIn("personas/technical/security.md", self.errors_text())

    def test_technical_persona_missing_heading(self):
        self.edit("personas/technical/scalability.md", "## Your angle\n")
        self.assertTrue([e for e in validate(self.root) if "technical/scalability" in e])

    def test_extra_technical_persona_rejected(self):
        write(self.root / "personas" / "technical" / "extra.md", "x")
        self.assertIn("personas/technical/extra.md", self.errors_text())

    def test_technical_persona_not_listed_in_skill_md(self):
        self.edit("SKILL.md", "already-solved", "")
        self.assertIn("already-solved", self.errors_text())

    def test_technical_research_agent_needs_output_heading(self):
        self.edit("research-agent-technical.md", "## Output")
        self.assertIn("research-agent-technical.md", self.errors_text())

    def test_missing_technical_eval_fixture(self):
        (self.root / "evals" / "technical-idea.md").unlink()
        self.assertIn("technical-idea.md", self.errors_text())

    def test_persona_not_listed_in_skill_md(self):
        self.edit("SKILL.md", "veteran", "")
        self.assertIn("veteran", self.errors_text())

    def test_template_missing_placeholder(self):
        self.edit("report-template.md", "{{objections}}\n")
        self.assertIn("{{objections}}", self.errors_text())

    def test_research_agent_needs_output_heading(self):
        self.edit("research-agent.md", "## Output")
        self.assertIn("research-agent.md", self.errors_text())

    def test_missing_edge_case_heading(self):
        self.edit("SKILL.md", "### Draft too short")
        self.assertIn("### Draft too short", self.errors_text())

    def test_missing_eval_fixture(self):
        (self.root / "evals" / "quit-todo-apps.expected.md").unlink()
        self.assertIn("quit-todo-apps.expected.md", self.errors_text())

    def test_cli_exit_codes(self):
        ok = subprocess.run([sys.executable, str(SCRIPT), str(self.root)], capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0)
        self.assertEqual(ok.stdout.strip(), "OK")
        (self.root / "SKILL.md").unlink()
        bad = subprocess.run([sys.executable, str(SCRIPT), str(self.root)], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("SKILL.md", bad.stdout)


if __name__ == "__main__":
    unittest.main()
