---
name: query-optimizer
description: Optimize SQL queries for performance and index efficiency. Use when reviewing slow queries, execution plans, database access patterns, or schema changes that affect index usage, join strategy, filtering, sorting, or pagination.
---

# Query Optimizer

## When to Use This Skill

Use this skill when tuning SQL for lower latency, better throughput, and more predictable index usage.

## Prerequisites

- The query text or execution plan being reviewed
- The table schema and available indexes
- The expected result size and access pattern

## Goal

Improve query performance by reducing unnecessary scans, minimizing row reads, and aligning predicates, joins, and sort order with available indexes.

## What to Look For

- Full table scans where selective indexes should be used
- Queries that prevent index usage because of functions, casts, leading wildcards, or non-sargable predicates
- Inefficient joins, correlated subqueries, or repeated lookups
- Sorting or grouping that forces large temporary operations
- Pagination patterns that degrade on large offsets
- Overly broad selects that fetch columns the caller does not need

## Step-by-Step Workflows

1. Read the query in the context of its filter, join, and access pattern.
2. Check which predicates are selective and whether they match an index prefix.
3. Identify clauses that block index use or force extra work.
4. Compare the query shape to the expected result cardinality.
5. Recommend the smallest change that improves the plan without changing behavior.

## Index Usage Heuristics

- Equality predicates on leading columns are the strongest index candidates.
- Range predicates can still use indexes, but later columns in a composite index may not help.
- `ORDER BY` is best supported when it matches the index order.
- Functions on indexed columns often prevent direct index access.
- Low-selectivity indexes may not help if the table is small or the filter is broad.

## Recommended Fixes

- Rewrite predicates to be sargable where possible.
- Add or adjust composite indexes to match the most common filter and sort patterns.
- Replace `SELECT *` with a narrower projection when only a subset of columns is needed.
- Break large offset pagination into keyset pagination when appropriate.
- Use query refactoring before adding more indexes if the SQL shape is the real problem.

## Output Standard

For each issue, provide:

- Query or location
- Performance symptom
- Why the current plan is inefficient
- Recommended SQL or index change
- Tradeoff or validation note

## Reporting Style

- Be concrete about the access path, not just the syntax.
- Prefer changes that improve both runtime and plan stability.
- Call out when an index helps one query but may slow writes or increase storage.

## Troubleshooting

- If the plan is unclear, confirm the actual predicate selectivity first.
- If an index change is proposed, check write amplification and storage cost.
- If the query still scans, rewrite the predicate shape before adding more indexes.

## References

- Database schema and execution-plan references
- Related indexing or query-design standards
