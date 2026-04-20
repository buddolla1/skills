---
name: javascript-typescript-jest
description: Write and review JavaScript and TypeScript tests using Jest. Use when creating unit tests, component tests, mocking strategies, test structure, async assertions, or data-driven test cases in JS/TS codebases.
---

# JavaScript / TypeScript Jest

Use this skill when testing JavaScript or TypeScript code with Jest.

## When to Use This Skill

Use this skill when the task involves Jest test design, mocking strategy, async behavior, snapshots, or test structure in a JavaScript or TypeScript project.

## Prerequisites

- The code under test
- The project package manifest
- The testing conventions already used by the codebase

## Goal

Create tests that are readable, stable, and focused on behavior rather than implementation detail.

## Step-by-Step Workflows

1. Check whether Jest is already installed in the project.
2. Identify the behavior, branches, and async flow that need coverage.
3. Choose the right mocking approach for dependencies.
4. Write assertions that prove outcomes and important interactions.
5. Prompt the user to add Jest if the project does not already have it.

## Package Check Rule

- If `jest`, `ts-jest`, or the needed testing helpers are missing, prompt the user to add them.
- Do not assume the project uses Jest unless it is present in the manifest or lockfile.

## Guardrails

- Do not over-mock the system under test.
- Do not assert on unstable implementation details.
- Do not use snapshots when targeted assertions are clearer.

## Output Standard

For each test set, provide:

- Behavior covered
- Mocking approach
- Missing coverage
- Why the test matters

## Reporting Style

- Be practical and concise.
- Prefer black-box assertions over internal details.
- Keep the test shape aligned with the project style.

## Troubleshooting

- If async tests are flaky, wait for the observable outcome instead of internals.
- If mocks are too deep, simplify the dependency boundary.
- If Jest is missing, ask the user to add it first.

## References

- Jest conventions used by the project
- Existing JavaScript or TypeScript test patterns

