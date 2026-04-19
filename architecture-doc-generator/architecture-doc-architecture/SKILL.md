---
name: architecture-doc-architecture
description: Generates architecture documentation for Java or Spring systems. Use when the user wants only the architecture doc or the architecture portion of a larger documentation set.
---

# Architecture Document

Use this skill to describe the system architecture at a durable, reviewable level.

## When to Use This Skill

Use this skill when the user wants an architecture document, system overview, component map, flow descriptions, or runtime boundaries.

## Prerequisites

- The intended audience for the document
- The source of truth from code, config, or deployment artifacts
- Any existing docs or diagrams that should be updated instead of duplicated

## Goal

Produce an architecture document that reflects the real system, its boundaries, its dependencies, and the tradeoffs behind it.

## Output Standard

Provide:

- Document type
- Audience
- Source of truth used
- Key content sections
- Any open assumptions or update points

## Recommended Sections

- Project overview
- System context
- Components
- Flows
- Dependencies
- Operational concerns
- Findings
- Recommendations

## Guardrails

- Do not write aspirational architecture as if it were implemented.
- Do not copy code comments or commit messages into documentation.
- Do not bury the main architecture in long narrative text.
- Prefer concise, maintainable docs over exhaustive prose.

## Output Location

- Write generated Markdown documents to the repository `doc/` folder unless the user explicitly requests a different path.
- Create `doc/` first if it does not exist.

## Reporting Style

- Be factual and specific about what exists.
- Prefer decision records over vague design descriptions.
- Keep docs easy to scan, maintain, and compare over time.

## References

- Existing repository docs and diagrams
- Related design notes
- The coordinator skill
