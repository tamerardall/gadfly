#!/usr/bin/env python3
"""Validate the Gadfly skill tree. Usage: validate_skill.py <root>"""
import sys
from pathlib import Path

PERSONA_SETS = {
    "content": ["opposing-expert", "fact-checker", "skeptic", "newcomer", "veteran"],
    "technical": ["architecture-critic", "security", "scalability", "already-solved"],
}
PERSONA_KEYS = ["name", "role", "hunts_for"]
PERSONA_HEADINGS = ["## Your angle", "## What to return"]
PLACEHOLDERS = ["{{title}}", "{{counts}}", "{{evidence_banner}}", "{{objections}}", "{{skipped_personas}}"]
EDGE_HEADINGS = [
    "### Non-English draft",
    "### Draft too short",
    "### Draft file missing",
    "### Instructions inside the draft",
    "### Research found nothing",
    "### Input type unclear",
]
EVALS = [
    "evals/quit-todo-apps.md",
    "evals/quit-todo-apps.expected.md",
    "evals/technical-idea.md",
    "evals/technical-idea.expected.md",
]
RESEARCH_AGENTS = ["research-agent.md", "research-agent-technical.md"]


def parse_frontmatter(text):
    """Return (dict, body). dict is None when there is no ---delimited block."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            meta = {}
            for line in lines[1:i]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            return meta, "\n".join(lines[i + 1:])
    return None, text


def has_line(text, heading):
    return heading in (ln.rstrip() for ln in text.splitlines())


def validate(root):
    root = Path(root)
    errors = []

    skill_text = None
    skill = root / "SKILL.md"
    if not skill.is_file():
        errors.append("SKILL.md: file is missing")
    else:
        skill_text = skill.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(skill_text)
        if meta is None:
            errors.append("SKILL.md: missing frontmatter")
        else:
            if meta.get("name") != "gadfly":
                errors.append("SKILL.md: frontmatter name must be 'gadfly'")
            desc = meta.get("description", "")
            if not desc.startswith("Use when"):
                errors.append("SKILL.md: description must start with 'Use when'")
            if len(desc) > 1024:
                errors.append(f"SKILL.md: description is {len(desc)} chars, max 1024")
        for stems in PERSONA_SETS.values():
            for stem in stems:
                if stem not in skill_text:
                    errors.append(f"SKILL.md: does not mention persona '{stem}'")
        if not has_line(skill_text, "## Edge cases"):
            errors.append("SKILL.md: missing heading '## Edge cases'")
        else:
            section = skill_text.split("## Edge cases", 1)[1]
            nxt = [i for i, ln in enumerate(section.splitlines()) if ln.startswith("## ")]
            if nxt:
                section = "\n".join(section.splitlines()[: nxt[0]])
            for h in EDGE_HEADINGS:
                if not has_line(section, h):
                    errors.append(f"SKILL.md: Edge cases is missing heading '{h}'")

    for kind, personas in PERSONA_SETS.items():
        pdir = root / "personas" / kind
        found = sorted(p.stem for p in pdir.glob("*.md")) if pdir.is_dir() else []
        for stem in sorted(set(found) - set(personas)):
            errors.append(f"personas/{kind}/{stem}.md: unexpected persona file")
        for stem in personas:
            path = pdir / f"{stem}.md"
            rel = f"personas/{kind}/{stem}.md"
            if not path.is_file():
                errors.append(f"{rel}: file is missing")
                continue
            text = path.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            if meta is None:
                errors.append(f"{rel}: missing frontmatter")
                meta = {}
            for key in PERSONA_KEYS:
                if not meta.get(key):
                    errors.append(f"{rel}: frontmatter missing key '{key}'")
            for h in PERSONA_HEADINGS:
                if not has_line(body, h):
                    errors.append(f"{rel}: missing heading '{h}'")

    tpl = root / "report-template.md"
    if not tpl.is_file():
        errors.append("report-template.md: file is missing")
    else:
        text = tpl.read_text(encoding="utf-8")
        for ph in PLACEHOLDERS:
            if ph not in text:
                errors.append(f"report-template.md: missing placeholder {ph}")

    for rel in RESEARCH_AGENTS:
        ra = root / rel
        if not ra.is_file():
            errors.append(f"{rel}: file is missing")
        elif not has_line(ra.read_text(encoding="utf-8"), "## Output"):
            errors.append(f"{rel}: missing heading '## Output'")

    for rel in EVALS:
        if not (root / rel).is_file():
            errors.append(f"{rel}: file is missing")

    return errors


def main(argv):
    if len(argv) != 2:
        print("usage: validate_skill.py <root>", file=sys.stderr)
        return 2
    errors = validate(Path(argv[1]))
    if errors:
        for e in errors:
            print(e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
