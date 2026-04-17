---
name: architecture-doc-generator
description: Generate README files, architecture documentation, and ADRs. Use when documenting Java or Spring systems, explaining service boundaries, design decisions, dependencies, deployment flow, or system behavior for engineers and stakeholders.
---

# Architecture Doc Generator

## When to Use This Skill

Use this skill when creating durable technical documentation for a system or significant change.

## Prerequisites

- The intended audience for the document
- The source of truth from code, config, or deployment artifacts
- Any existing docs or diagrams that should be updated instead of duplicated

## Goal

Produce documentation that reflects the real system, the actual design decisions, and the tradeoffs behind them.

## What to Generate

- README content for setup, usage, and local development
- Architecture docs for system context, components, flows, and dependencies
- ADRs for decisions, alternatives, consequences, and status

## Step-by-Step Workflows

1. Identify the intended audience and the decision being documented.
2. Gather the source of truth from code, configs, deployment, and existing docs.
3. Capture the current architecture before describing the desired state.
4. Distill decisions, constraints, and tradeoffs into concise artifacts.
5. Keep the document actionable, accurate, and easy to update.

## README Guidance

- Explain what the system does and how to run it.
- Include prerequisites, configuration, and common workflows.
- Keep setup steps concrete and current.
- Avoid architecture jargon unless it helps the reader operate the project.

## Architecture Doc Guidance

- Describe context, components, interfaces, and data flow.
- Show dependencies, runtime boundaries, and operational concerns.
- Explain why the system is structured the way it is.
- Include diagrams or structured sections when they improve clarity.

## ADR Guidance

- State the decision clearly and in the present tense.
- Record alternatives considered and the reason for the chosen option.
- Capture consequences, risks, and follow-up work.
- Keep the scope to a single meaningful decision.

## Guardrails

- Do not write aspirational architecture as if it were implemented.
- Do not copy code comments or commit messages into documentation.
- Do not bury decisions in long narrative text.
- Prefer concise, maintainable docs over exhaustive prose.

## Output Standard

For each document, provide:

- Document type
- Audience
- Source of truth used
- Key content sections
- Any open assumptions or update points

## Reporting Style

- Be factual and specific about what exists.
- Prefer decision records over vague design descriptions.
- Keep docs easy to scan, maintain, and compare over time.

## Troubleshooting

- If the document describes future intent, verify whether it is actually implemented.
- If the source of truth is missing, collect it before drafting.
- If the doc is getting long, split it into a README, architecture view, and ADR.

## References

- Existing repository docs and diagrams
- Related ADRs and design notes
