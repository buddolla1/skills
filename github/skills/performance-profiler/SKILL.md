---
name: performance-profiler
description: Profile application performance to identify bottlenecks and recommend targeted fixes. Use when analyzing slow requests, high latency, CPU or memory pressure, blocking I/O, inefficient loops, cacheable work, or opportunities for caching and async processing.
---

# Performance Profiler

## When to Use This Skill

Use this skill when a system is slow and the task is to identify the real bottleneck before proposing an optimization.

## Prerequisites

- The slow request, job, or endpoint being analyzed
- Any available metrics, traces, or logs for the hot path
- Knowledge of whether the bottleneck is CPU, I/O, or contention

## Goal

Find the highest-cost path in the workload, explain why it is slow, and recommend the smallest safe improvement with the best return on effort.

## What to Look For

- Repeated work in hot paths
- Blocking network, file, or database calls on request threads
- Expensive computations that are deterministic and reusable
- Serialization, mapping, or transformation overhead
- Thread contention, lock waits, or queue buildup
- Unbounded fan-out, chatty dependencies, or sequential waits

## Step-by-Step Workflows

1. Identify the slow user flow, job, or endpoint.
2. Separate CPU cost, I/O wait, and contention.
3. Trace the critical path and measure repeated work.
4. Find candidates for caching, batching, parallelism, or async offloading.
5. Recommend the simplest change that removes the dominant bottleneck.

## When to Suggest Caching

- The same expensive result is recomputed repeatedly.
- The underlying data changes less frequently than it is read.
- The cache key is stable and the invalidation rule is clear.
- The cost of a miss is acceptable and stale data is tolerable within bounds.

## When to Suggest Async Processing

- The work does not need to complete before returning to the caller.
- The task is I/O-bound, long-running, or bursty.
- The request path can return an accepted or eventual result.
- There is a durable retry and failure-handling model.

## Guardrails

- Do not add caching without a clear invalidation strategy.
- Do not make work async if the caller still blocks on the result.
- Prefer measurement over intuition.
- Treat premature parallelism as a risk, not a default optimization.

## Output Standard

For each issue, provide:

- Bottleneck location
- Evidence or symptom
- Root cause
- Recommended fix
- Tradeoff or validation note

## Reporting Style

- Be specific about the bottleneck class: CPU, I/O, contention, or redundant work.
- Prefer changes that reduce end-to-end latency, not just local micro-optimizations.
- Explain why caching or async processing fits the workload before recommending it.

## Troubleshooting

- If the bottleneck is not measurable, gather evidence before optimizing.
- If caching is proposed, confirm the invalidation strategy and data freshness needs.
- If async processing is proposed, verify the caller does not still block on completion.

## References

- Performance metrics and traces for the workload
- Related caching or async design notes
