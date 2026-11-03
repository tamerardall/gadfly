# Expected: evals/quit-todo-apps.md

Run: `Use the gadfly skill on evals/quit-todo-apps.md`

## Objection classes that must appear (at least one objection each)

- [ ] No metric or baseline: "doubled productivity" is never defined or measured.
- [ ] Sample of one: the claim rests on a single person's experience.
- [ ] Unspecified replacement system: the draft never says what replaced the apps (how tasks are tracked or remembered).

## Report-shape checklist

- [ ] Report is printed in the chat; no file is written.
- [ ] A title, a count line (like `N objections: x HIGH, y MED, z LOW`) and exactly one evidence banner are present.
- [ ] Every objection has a text severity label `[HIGH]`, `[MED]` or `[LOW]`.
- [ ] Every objection has a Why line, an Evidence line (`research - <bare URL>` or `persona (simulated)`) and a one-sentence imperative Fix.
- [ ] Sorted HIGH, then MED, then LOW; at most 10 objections; no duplicates.
- [ ] `research` evidence appears only with a URL; otherwise `persona (simulated)`.
- [ ] The research subagent ran first; the five persona calls were dispatched in one message (parallel), if observable.
- [ ] With web search unavailable: the banner is the simulation-only string (`Simulation only: web research failed (...)`) and no objection claims research evidence.
