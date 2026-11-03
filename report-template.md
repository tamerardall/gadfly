<!--
Gadfly report template. Fill every {{placeholder}}; SKILL.md supplies the values.

{{counts}} looks like: 3 objections: 1 HIGH, 1 MED, 1 LOW

Each objection in {{objections}} is rendered as this block. Severity is always a
text label, one of HIGH, MED, LOW:

### [HIGH] <title>
Why: <what in the draft triggers it>
Evidence: research - <source link>   (or: persona (simulated))
Fix: <one imperative sentence>

{{skipped_personas}}: when empty, omit the whole "Skipped personas" section
(heading included).
-->

# {{title}}

{{counts}}

{{evidence_banner}}

## Objections

{{objections}}

## Skipped personas

{{skipped_personas}}
