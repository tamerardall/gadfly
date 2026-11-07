# Expected: evals/technical-idea.md

Run: `Use the gadfly skill on evals/technical-idea.md`

The input is a technical proposal, so the `technical` set must run (research-agent-technical.md, four personas: architecture-critic, security, scalability, already-solved).

## Objection classes that must appear (at least one objection each)

- [ ] Already solved: existing open-source or self-hosted options (for example pgvector, Qdrant, FAISS) cover the need; the build-vs-buy choice is never explained.
- [ ] Unstated load and scale assumptions: brute-force scan over a single in-memory server, "queries stay fast at tenfold growth" is asserted, not measured.
- [ ] Security and tenancy: no authentication, all customers in one shared index, user text passed straight to the query endpoint.
- [ ] Durability or operations: nightly snapshot only (data loss window), no replication, no backup or monitoring story, four-week estimate ignores ongoing maintenance.

## Report-shape checklist

- [ ] Report is printed in the chat; no file is written.
- [ ] A title, a count line (like `N objections: x HIGH, y MED, z LOW`) and exactly one evidence banner are present.
- [ ] Every objection has a text severity label `[HIGH]`, `[MED]` or `[LOW]`, a Why line, an Evidence line and a one-sentence imperative Fix.
- [ ] Sorted HIGH, then MED, then LOW; at most 10 objections; no duplicates.
- [ ] `research` evidence appears only with a URL (a GitHub issue, competing project or discussion); otherwise `persona (simulated)`.
- [ ] The technical research subagent ran first; exactly four persona calls were dispatched in one message (parallel), if observable.
- [ ] A one-line note names the type used ("technical") because the user did not state it.
- [ ] With web search unavailable: the banner is the simulation-only string and no objection claims research evidence.
