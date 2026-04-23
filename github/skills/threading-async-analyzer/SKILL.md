---
name: threading-async-analyzer
description: Analyze Java threading and async code for blocking calls, thread starvation risk, and missed concurrency opportunities. Use when reviewing Spring Boot services, task execution, or request flows for blocking I/O, synchronous waits, and opportunities to use @Async or CompletableFuture safely.
---

# Threading / Async Analyzer

## When to Use This Skill

Use this skill when reviewing Java concurrency code or request paths that may be blocking request threads unnecessarily.

## Prerequisites

- The thread, executor, or request path being reviewed
- The blocking call or wait point under suspicion
- Any timeout, pool, or queue configuration that affects concurrency

## Goal

Identify the operations that hold threads longer than necessary, explain the bottleneck, and recommend the safest async pattern for the workload.

## What to Detect

- Blocking I/O on request threads
- Synchronous remote calls that could be deferred or parallelized
- `join()`, `get()`, or other waits that erase async benefits
- Long-running work inside controllers, services, listeners, or schedulers
- Thread pool exhaustion, deadlock risk, or unbounded task submission
- Async code that still behaves synchronously due to hidden waits or shared locks

## Step-by-Step Workflows

1. Identify which thread owns the work and which thread waits for the result.
2. Trace the call chain for blocking network, database, file, or external service calls.
3. Determine whether the caller truly needs an immediate result.
4. Check executor usage, queueing behavior, and exception handling.
5. Recommend the least risky concurrency change that removes the blocking path.

## When to Suggest `@Async`

- The work is fire-and-forget or completion can happen after the response.
- The task can run independently and does not require the request thread.
- There is a configured executor with sensible limits.
- Failure handling and observability are defined.

## When to Suggest `CompletableFuture`

- Independent tasks can run in parallel and be combined later.
- The code needs explicit composition, timeout control, or fallback handling.
- The implementation benefits from non-blocking orchestration rather than annotation-based dispatch.

## Guardrails

- Do not use async to hide slow code that still waits before returning.
- Do not introduce more threads than the workload and executor can support.
- Avoid async boundaries around shared mutable state unless the concurrency model is clear.
- Prefer clear ownership of completion, timeout, and failure handling.

## Output Standard

For each issue, provide:

- Location
- Blocking point
- Why it harms throughput or latency
- Recommended async approach
- Risk or validation note

## Reporting Style

- Be specific about where the thread is blocked and what is waiting.
- Prefer solutions that reduce request-thread occupancy and preserve correctness.
- Explain why `@Async` or `CompletableFuture` is the right shape for the problem, not just the syntax.

## Troubleshooting

- If the async code still waits synchronously, remove the blocking join or get path first.
- If the executor is saturated, tune the pool before adding more concurrency.
- If the work shares mutable state, validate thread safety before recommending parallelism.

## References

- Executor and async configuration for the service
- Related threading or performance documentation
