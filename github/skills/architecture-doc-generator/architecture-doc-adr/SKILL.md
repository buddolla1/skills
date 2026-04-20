---
name: architecture-doc-adr
description: Creates ADRs for Java or Spring systems. Use when the user wants a decision record, tradeoff analysis, or the ADR portion of a larger documentation set.
---

# Architecture ADR

Use this skill to record a meaningful architecture decision.

## When to Use This Skill

Use this skill when the user wants an ADR, a decision record, or a concise explanation of an architectural choice.

## Prerequisites

- The decision being documented
- The alternatives considered
- The source of truth from code, config, or design notes

## Goal

Capture one meaningful decision with its context, rationale, consequences, and follow-up work.

## Output Standard

Provide:

- Decision
- Context
- Alternatives considered
- Consequences
- Status
- Follow-up work

## Guardrails

- Keep the scope to a single decision.
- Do not bury the recommendation in analysis.
- Do not write future intent as if it is already implemented.

## Output Location

- Write generated Markdown documents to the repository `doc/` folder unless the user explicitly requests a different path.
- Create `doc/` first if it does not exist.

## Reporting Style

- Be concise and decision-oriented.
- Prefer explicit tradeoffs over vague design prose.

## References

- Existing repository docs and design notes
- The coordinator skill
