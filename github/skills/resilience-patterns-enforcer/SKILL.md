---
name: resilience-patterns-enforcer
description: Enforce resilient Java service patterns using Resilience4j. Use when reviewing Spring Boot integrations for circuit breaker, retry, and bulkhead needs around unstable dependencies, timeouts, transient failures, and downstream overload protection.
---

# Resilience Patterns Enforcer

## When to Use This Skill

Use this skill when hardening service-to-service or service-to-infrastructure calls against failure and overload.

## Prerequisites

- The downstream dependency and failure mode being addressed
- The timeout, retry, or fallback behavior already in place
- Any operational metrics that show how the dependency fails under load

## Goal

Apply resilience patterns where they actually reduce blast radius, improve availability, and prevent cascading failure.

## Patterns to Add

- Circuit breaker for unstable or frequently failing dependencies
- Retry for transient failures with bounded attempts and backoff
- Bulkhead for isolating resource pools and preventing overload spread

## Step-by-Step Workflows

1. Identify the dependency that fails, times out, or saturates under load.
2. Classify the failure mode: transient, persistent, or overload.
3. Choose the narrowest pattern that addresses the failure.
4. Verify timeout, fallback, and exception handling behavior together.
5. Check that metrics and logs make resilience behavior observable.

## Circuit Breaker Guidance

- Use it when repeated failures should stop wasting time and resources.
- Configure thresholds from observed failure behavior, not guesses.
- Pair it with a fallback or fast failure path.
- Ensure the recovery window is long enough to avoid flapping.

## Retry Guidance

- Use it only for transient failures that may succeed on a later attempt.
- Keep retry counts bounded and use backoff with jitter where appropriate.
- Do not retry non-idempotent operations unless the business semantics allow it.
- Avoid retrying when the dependency is already overloaded or timing out consistently.

## Bulkhead Guidance

- Use it to isolate critical workloads from noisy neighbors.
- Separate thread pools or resource limits for distinct dependency groups.
- Prevent one slow integration from consuming all available capacity.
- Tune bulkheads to match business priority and traffic shape.

## Guardrails

- Do not stack patterns blindly on every call.
- Do not retry through a circuit breaker failure without a clear policy.
- Do not add bulkheads without understanding the concurrency model.
- Prefer timeouts as the first line of defense before retries or circuit breaking.

## Output Standard

For each issue, provide:

- Dependency or call site
- Failure mode
- Recommended resilience pattern
- Why the pattern fits the risk
- Operational tradeoff or validation note

## Reporting Style

- Be specific about the downstream risk being reduced.
- Prefer explicit resilience policy over ad hoc error handling.
- Explain how the pattern changes behavior under failure and load.

## Troubleshooting

- If the dependency is failing persistently, a retry is usually the wrong first fix.
- If the workload is overloaded, start with timeouts and bulkheads before more retries.
- If the policy is unclear, define ownership for fallback and recovery behavior first.

## References

- Resilience4j configuration and project standards
- Downstream service reliability notes
