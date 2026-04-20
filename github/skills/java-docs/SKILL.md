---
name: java-docs
description: Document Java types with Javadoc comments and best practices. Use when adding or reviewing JavaDoc for classes, methods, parameters, return values, and exceptions.
---

# Java Docs

Use this skill when Java code needs clearer API documentation.

## When to Use This Skill

Use this skill when classes, methods, or APIs need Javadoc comments or when documentation quality is being reviewed.

## Prerequisites

- The Java types being documented
- The intended audience for the docs
- Any style or documentation rules used by the project

## Goal

Write documentation that explains intent, usage, and constraints without duplicating obvious code.

## Step-by-Step Workflows

1. Identify public or important internal APIs.
2. Document purpose, parameters, return values, and exceptions.
3. Focus on behavior and contract, not restating method names.
4. Keep comments current with the code.
5. Remove stale or misleading documentation.

## Guardrails

- Do not add comments that merely repeat the code.
- Do not document trivial getters or obvious behavior unless needed.
- Do not leave stale examples or outdated contracts.

## Output Standard

For each documented item, provide:

- Type or method
- Purpose
- Key contract details
- Any caution or limitation

## Reporting Style

- Be concise and useful.
- Document intent, not noise.
- Keep API contracts easy to understand.

## Troubleshooting

- If a comment is too long, trim it to the essential contract.
- If the code changed, update the docs immediately.
- If the API is ambiguous, clarify the behavior in the Javadoc.

## References

- JavaDoc conventions
- Project code documentation standards

