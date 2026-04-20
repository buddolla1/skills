---
name: feature-flag-manager
description: Manage feature flags with LaunchDarkly or configuration toggles. Use when planning rollouts, canary releases, kill switches, A/B enablement, environment-based switches, or cleanup of stale feature flags in Java and Spring Boot systems.
---

# Feature Flag Manager

## When to Use This Skill

Use this skill when introducing or reviewing feature flags for safe rollout and controlled exposure.

## Prerequisites

- The business purpose of the flag
- The flag evaluation source, such as LaunchDarkly or config toggles
- The default-state behavior when the flag is disabled or unavailable

## Goal

Use flags to reduce release risk, isolate blast radius, and support controlled delivery without creating long-lived operational debt.

## What to Enforce

- Clear flag purpose: rollout, experiment, kill switch, or environment toggle
- Targeted exposure using LaunchDarkly or config-based toggles
- Safe default behavior when a flag is off or unavailable
- Observable flag state for debugging and release support
- Cleanup plan for expired or fully rolled-out flags

## Step-by-Step Workflows

1. Identify the business reason for the flag.
2. Determine the evaluation source: LaunchDarkly, config, or service-side logic.
3. Check the default path and ensure it is safe for all environments.
4. Verify the flag is scoped narrowly enough for gradual rollout.
5. Define the removal condition so the flag does not become permanent.

## LaunchDarkly Guidance

- Keep flag keys stable and descriptive.
- Use targeting rules deliberately, not as a substitute for application logic.
- Ensure SDK initialization and fallback behavior are safe under outage conditions.
- Propagate flag evaluation where necessary for diagnostics and auditability.

## Config Toggle Guidance

- Use configuration toggles for coarse environment differences and operational switches.
- Keep toggle names explicit and document the default state.
- Avoid scattering the same flag check across many code paths.
- Centralize evaluation when multiple components need the same decision.

## Guardrails

- Do not introduce flags without a removal plan.
- Do not use flags to hide unresolved product or design decisions indefinitely.
- Do not let flag logic fragment the code path without clear ownership.
- Prefer a single source of truth for each decision point.

## Output Standard

For each issue, provide:

- Flag name or location
- Purpose of the flag
- Risk being controlled
- Recommended LaunchDarkly or config approach
- Cleanup or sunset note

## Reporting Style

- Be specific about the rollout or control objective.
- Prefer simple, observable flag logic over clever branching.
- Call out stale or ambiguous flags that should be removed or consolidated.

## Troubleshooting

- If a flag has no removal plan, treat it as technical debt.
- If the flag is used in many places, centralize evaluation.
- If the fallback path is unsafe, fix the default behavior before rollout.

## References

- LaunchDarkly project conventions
- Environment configuration standards
