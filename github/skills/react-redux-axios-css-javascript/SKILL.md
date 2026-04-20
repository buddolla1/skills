---
name: react-redux-axios-css-javascript
description: Build and review React JavaScript projects that use Redux, Axios, and CSS. Use when creating or maintaining state management, HTTP integration, component styling, reducers, selectors, request flows, or layout and responsive design in JavaScript React apps.
---

# React Redux Axios CSS JavaScript

Use this skill when working on React JavaScript applications that combine Redux state, Axios API calls, and CSS styling.

## When to Use This Skill

Use this skill when the task involves React components, Redux state flow, Axios requests, or CSS styling in a JavaScript project. If the project does not already have the required packages, prompt the user to add them first.

## Prerequisites

- The React files being reviewed
- The project package manifest
- The state, API, and styling approach already used

## Goal

Create maintainable React JavaScript implementations that keep state, data fetching, and styling predictable.

## Step-by-Step Workflows

1. Check whether Redux, Axios, and CSS tooling are already installed.
2. Map the state slices, API requests, and components that use them.
3. Keep reducers pure, request flow centralized, and CSS maintainable.
4. Verify responsive behavior and avoid duplicated or conflicting state.
5. Prompt the user to add missing packages before depending on them.

## Package Check Rule

- If `redux`, `react-redux`, `axios`, or the needed CSS tooling are missing, prompt the user to add them.
- Do not assume the project has state, HTTP, or styling libraries unless the manifest shows them.

## Guardrails

- Do not mutate Redux state directly.
- Do not scatter Axios config across multiple components.
- Do not overuse inline styles when reusable CSS is clearer.
- Do not add duplicate state when one source of truth is enough.

## Output Standard

For each area, provide:

- State slice, request flow, or style area
- Problem or improvement
- Why it matters
- Recommended change

## Reporting Style

- Be practical and specific.
- Prefer simple, shared patterns over repetition.
- Tie advice to maintainability, readability, and predictable UI behavior.

## Troubleshooting

- If state is duplicated, consolidate it.
- If request handling is repeated, centralize the client.
- If styles are hard to maintain, organize them by component or domain.
- If packages are missing, ask the user to add them first.

## References

- Redux, Axios, and CSS conventions used by the project
- Existing React state, API, and styling patterns

