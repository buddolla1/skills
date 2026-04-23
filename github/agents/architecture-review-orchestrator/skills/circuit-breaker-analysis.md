# Skill: circuit-breaker-analysis

## Description
Evaluate circuit breaker usage, thresholds, fallback behavior, and downstream protection.

## When to use
Use this skill when code calls external services, queues, databases, or remote APIs that can fail or degrade.

## Instructions
- Check whether circuit breakers exist where needed.
- Review threshold configuration and open/half-open behavior.
- Assess fallback correctness and business safety.
- Flag missing isolation from unstable dependencies.

## Output Format
- Circuit Breaker Issue
- Severity
- Evidence
- Risk
- Recommended Fix
