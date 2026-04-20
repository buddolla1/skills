---
name: architecture-doc-generator
description: Coordinates README, architecture documentation, and ADR creation into smaller skills. Use when documenting Java or Spring systems and you want progressive loading for README, architecture docs, ADRs, or a full documentation set.
---

# Architecture Doc Generator

Use this skill as the coordinator for durable technical documentation.

## When to Use This Skill

Use this skill when the user asks for documentation, architecture analysis, design decisions, or a complete document set for a Java or Spring system.

## First Question

Ask the user what they want to create first:

- README
- Architecture doc
- ADR
- Full doc

If the request does not specify one of these, ask this question before proceeding.

## Progressive Loading Model

1. Load `create-readme/SKILL.md` when the user wants a README.
2. Load [architecture-doc-architecture](architecture-doc-architecture/SKILL.md) when the user wants an architecture document.
3. Load [architecture-doc-adr](architecture-doc-adr/SKILL.md) when the user wants an ADR.
4. For a full doc, load the relevant smaller skills in sequence based on the requested document set.

## Source of Truth

- Prefer real source files over generated or build output.
- Inspect code, config, deployment artifacts, and existing docs.
- Do not invent architecture or decisions that are not supported by the repository.

## Guardrails

- Do not generate the full doc until the user explicitly asks for it.
- Do not mix README, architecture, and ADR content unless the user asked for a combined document.
- Do not bury decisions in long narrative text.
- Do not duplicate existing docs without checking whether they should be updated instead.

## References

- The source code and configuration of the project
- The specialized documentation skills in this directory
