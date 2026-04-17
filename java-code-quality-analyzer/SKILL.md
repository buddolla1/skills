---
name: java-code-quality-analyzer
description: Analyze Java code for quality issues, maintainability risks, and refactoring opportunities. Use when reviewing Java classes, service layers, Spring Boot code, or PR diffs for code smells, long methods, duplicate logic, readability problems, and concrete fixes.
---

# Java Code Quality Analyzer

## When to Use This Skill

Use this skill when assessing Java code quality and recommending pragmatic refactors.

## Prerequisites

- The class, method, or diff being reviewed
- The behavior that must remain unchanged
- Any tests or examples that show the intended design

## Goal

Identify maintainability problems early, explain the impact in business terms, and suggest fixes that are safe, incremental, and easy to validate.

## What to Look For

- Code smells that increase cognitive load or defect risk
- Long methods or methods with multiple responsibilities
- Duplicate logic or copy-pasted branching
- Poor naming, unclear abstractions, and hidden side effects
- Excessive coupling, deep nesting, or weak separation of concerns
- Defensive patterns that should be simplified or extracted

## Step-by-Step Workflows

1. Read the change in context, not in isolation.
2. Identify the primary responsibility of each class and method.
3. Flag only findings that have a meaningful maintainability, correctness, or testability impact.
4. Prefer root-cause analysis over symptom-only comments.
5. Recommend the smallest safe refactor that improves the design.

## Detection Heuristics

- A method that mixes validation, transformation, orchestration, and persistence is too broad.
- Repeated conditionals, mapping logic, or request/response shaping usually belongs in a shared function or helper.
- Code that is hard to name is often doing too much.
- Deep nesting, boolean flags, and chained null checks usually indicate missing structure.
- Large blocks that differ only by literals or minor branching are candidates for parameterization.

## Suggesting Fixes

- Extract method when one block has a single clear subtask.
- Extract class when a concept has its own lifecycle, rules, or dependencies.
- Replace duplication with a shared helper only when the abstraction is stable and obvious.
- Simplify control flow before introducing new patterns.
- Keep refactors incremental; avoid large redesigns unless the code already has multiple linked problems.

## Output Standard

For each issue, provide:

- Location
- Why it matters
- Recommended fix
- Risk if ignored

## Reporting Style

- Be specific, not generic.
- Prefer examples from the code over abstract advice.
- Separate real defects from code-style preferences.
- Do not propose refactors that only move code around without reducing complexity.

## Troubleshooting

- If the code smells are stylistic only, do not overstate the issue.
- If a refactor changes behavior, keep it incremental and add tests first.
- If the abstraction is unclear, verify whether the code is doing too much rather than splitting it prematurely.

## References

- Related code review notes and project conventions
- Java and Spring style guidance used by the team
