---
name: java-junit
description: Get best practices for JUnit 5 unit testing for Java. Use when creating or reviewing unit tests, including data-driven tests, assertions, fixtures, and test structure.
---

# Java JUnit

Use this skill when writing Java unit tests with JUnit 5.

## When to Use This Skill

Use this skill when the task is to write, review, or improve JUnit-based unit tests.

## Prerequisites

- The class or method under test
- The behavior that must be validated
- Any existing test conventions in the project

## Goal

Create readable, reliable JUnit tests that protect important behavior.

## Step-by-Step Workflows

1. Identify the behavior and branch structure.
2. Choose the right assertion and fixture style.
3. Cover happy path, edge cases, and failure paths.
4. Keep test names descriptive and stable.
5. Avoid testing implementation details unless they matter.

## Guardrails

- Do not overfit tests to internal code structure.
- Do not repeat setup unnecessarily.
- Do not add low-value assertions that do not prove behavior.

## Output Standard

For each test set, provide:

- Behavior covered
- Missing branches
- Assertion strategy
- Risk if untested

## Reporting Style

- Be behavior-focused.
- Prefer clear test names.
- Keep fixtures simple and maintainable.

## Troubleshooting

- If the tests are hard to read, simplify the setup.
- If branches are missing, add targeted scenarios.
- If data-driven tests help, use them for repeated cases.

## References

- Project testing conventions
- Existing test patterns in the codebase

