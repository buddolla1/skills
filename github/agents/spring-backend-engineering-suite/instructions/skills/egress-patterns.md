# Skill: egress-patterns

## Purpose
Detect reliability issues in outbound calls and integration paths.

## When To Use
Use this skill for REST clients, Kafka producers or consumers, DB access, Redis access, SDK usage, and external adapters.

## Instructions
- Check for missing timeout, retry, and fallback behavior.
- Check for poor error handling and missing correlation or trace propagation.
- Flag missing circuit breaker or bulkhead controls where the dependency is fragile.
- Flag unbounded calls and weak observability.

## Output
- Egress issue
- Severity
- File
- Failure impact
- Recommended fix
