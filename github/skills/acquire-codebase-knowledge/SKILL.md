---
name: acquire-codebase-knowledge
description: Map, document, and onboard into an existing codebase. Use when the user asks to understand a repository, identify relevant files, document architecture, or create codebase knowledge before making changes.
---

# Acquire Codebase Knowledge

Use this skill when the first task is to understand how a repository is structured before changing it.

## When to Use This Skill

Use this skill when the user asks to map a codebase, document architecture, onboard into a repository, or find the relevant modules before implementation.

## Prerequisites

- The repository or workspace to inspect
- The scope of the investigation
- Any specific feature, bug, or subsystem the user cares about

## Goal

Build an accurate picture of the codebase so later changes are targeted and safe.

## Step-by-Step Workflows

1. Identify the entry points, modules, and top-level structure.
2. Find the files, packages, and dependencies that matter to the task.
3. Summarize the architecture, boundaries, and ownership areas.
4. Highlight risks, unknowns, and places that need deeper review.
5. Hand back a clear map of where future work should happen.

## Guardrails

- Do not assume a file is relevant without checking the actual usage.
- Do not over-document low-value areas.
- Do not confuse onboarding notes with implementation guidance.

## Output Standard

For each area, provide:

- File or module
- Responsibility
- Why it matters
- Follow-up investigation needed

## Reporting Style

- Be factual and repository-specific.
- Prefer concise maps over long narratives.
- Call out the most relevant files first.

## Troubleshooting

- If the repository is large, start from package boundaries and entry points.
- If the architecture is unclear, map dependencies before summarizing.
- If a file seems important, verify how it is actually used.

## References

- Repository structure and package layout
- Existing architecture docs and READMEs

