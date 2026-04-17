---
name: create-specification
description: Create a specification file for a solution, feature, or workflow. Use when writing AI-friendly specs that define scope, behavior, constraints, acceptance criteria, and implementation notes.
---

# Create Specification

Use this skill when a feature or system needs a clear, structured specification before implementation.

## When to Use This Skill

Use this skill when the user asks for a spec, wants to define requirements, or needs a document that can guide implementation and review.

## Prerequisites

- The problem statement or feature idea
- The desired outcome and constraints
- Any existing requirements or examples

## Goal

Turn a request into a precise, implementation-ready specification.

## Step-by-Step Workflows

1. Clarify the scope and intended outcome.
2. Define the functional requirements and constraints.
3. Add acceptance criteria and non-goals.
4. Include implementation notes only when they are useful.
5. Keep the spec tight enough to review and maintain.

## Guardrails

- Do not mix vague ideas with confirmed requirements.
- Do not let the spec grow into a design essay.
- Do not omit acceptance criteria.

## Output Standard

For each spec, provide:

- Problem statement
- Scope
- Requirements
- Acceptance criteria
- Out of scope items

## Reporting Style

- Be precise and testable.
- Prefer structured bullets over paragraphs.
- Keep language implementation-neutral unless needed.

## Troubleshooting

- If the request is ambiguous, ask for scope before writing.
- If there are too many requirements, split them into phases.
- If implementation notes dominate, move detail to a design doc.

## References

- Related architecture docs and ADRs
- Existing product or feature requirements

