---
name: springboot-exception-orchestrator
description: Orchestrate exception-risk analysis across large Spring Boot codebases. Use when reviewing repositories for swallowed exceptions, broken rollback behavior, async exception leaks, REST error mapping gaps, logging omissions, and production reliability risks.
---

# Spring Boot Exception Orchestrator

## When to Use This Skill

Use this skill when the task is to analyze exception handling quality across a large Spring Boot codebase and produce a consolidated reliability review.

## Prerequisites

- The repository or module scope to analyze
- The exception-handling patterns already in use
- Any production failure symptoms, logs, or incidents that motivated the review

## Goal

Find exception-handling weaknesses systematically, deduplicate overlapping findings, and rank issues by production risk.

## What to Analyze

- Try/catch misuse and swallowed exceptions
- Exception rethrow patterns and loss of root cause
- `@ControllerAdvice` and REST error mapping
- Async, `CompletableFuture`, and executor exception leaks
- Transaction rollback behavior and `@Transactional` misuse
- Logging and observability gaps around failures
- Known enterprise anti-patterns that hide failure or reduce diagnosability

## Step-by-Step Workflows

1. Discover the repository shape, module boundaries, and file types relevant to exception handling.
2. Split the codebase into manageable chunks based on semantic ownership and risk area.
3. Review each chunk with the relevant exception concerns in mind.
4. Merge duplicate findings and keep the highest-severity interpretation.
5. Produce a consolidated report with ranked issues, fixes, and code-level recommendations.

## Scanning Roles

- File discovery: identify modules, packages, and high-risk areas
- Core Java exceptions: inspect try/catch blocks, rethrows, and wrapped exceptions
- Spring MVC exceptions: inspect controllers, advice, status mapping, and response bodies
- Async exceptions: inspect `@Async`, `CompletableFuture`, and executor boundaries
- Transaction safety: inspect rollback behavior and exception propagation
- Logging and observability: confirm failures are logged with actionable context
- Pattern intelligence: detect repeatable anti-patterns and framework misuse
- Risk scoring: prioritize issues by severity, reach, and production impact
- Report generation: summarize findings with fixes and code snippets when needed

## Aggregation Rules

- Deduplicate overlapping findings across files and modules.
- Prefer the most severe interpretation when multiple agents report the same issue.
- Keep related exception issues grouped by root cause.
- Distinguish local correctness issues from systemic reliability risks.

## Guardrails

- Do not report every catch block as a defect.
- Do not lose the original exception cause when recommending fixes.
- Do not split the review so far that cross-cutting exception patterns are missed.
- Keep findings actionable and tied to production behavior.

## Output Standard

For each issue, provide:

- Location
- Exception-handling concern
- Why it matters in production
- Recommended fix
- Severity or risk score

## Reporting Style

- Be concise, direct, and system-oriented.
- Prefer root-cause analysis over isolated syntax comments.
- Explain how the exception path behaves under load, retries, and rollback.

## Troubleshooting

- If too many findings overlap, consolidate them under the root failure mode.
- If a catch block is intentional, explain why it is safe and what context it preserves.
- If rollback behavior is unclear, trace the transaction boundary before reporting.

## References

- Spring Boot exception handling conventions
- Existing controller advice, logging, and transaction patterns in the codebase
