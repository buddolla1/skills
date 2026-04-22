# Architecture Review Orchestrator - JSON Overview

## Overview

This folder contains the machine-readable contract for the `Architecture Review Orchestrator`.

Primary file:

- [`architecture-review-orchestrator.json`](architecture-review-orchestrator.json)

## Purpose

The JSON defines the base orchestrator contract:

- orchestrator identity and version
- parallel-then-aggregate execution model
- six specialized agents
- markdown output schema

## Architecture Summary

The JSON expresses the core orchestration model:

- one orchestrator
- six pillar-specific agents
- parallel review execution
- result aggregation
- single final markdown report

## Reusable Skills

The orchestrator reuses shared skills to keep reviews consistent:

- `ddd-bounded-context-analysis` for domain modeling and boundary checks
- `circuit-breaker-analysis` for resilience and fault-tolerance review
- `caching-strategy-evaluator` for scalability and performance review
- `api-maturity-check` for API governance review
- `observability-checklist` for observability and operability review
- `adr-generator` for decision capture during aggregation
- `c4-diagram-generator` for Mermaid diagrams in the final report

## Flow Chart

```mermaid
flowchart TD
    A[Load JSON contract] --> B[Start orchestrator]
    B --> C[Dispatch six agents in parallel]
    C --> D[Structural integrity agent]
    C --> E[Domain modeling agent]
    C --> F[Resilience agent]
    C --> G[Scalability agent]
    C --> H[API governance agent]
    C --> I[Observability agent]
    D --> D1[ddd-bounded-context-analysis-skills]
    E --> D1
    F --> F1[circuit-breaker-analysis-skills]
    G --> G1[caching-strategy-evaluator-skills]
    H --> H1[api-maturity-check-skills]
    I --> I1[observability-checklist-skills]
    D1 --> J[Aggregate findings]
    F1 --> J
    G1 --> J
    H1 --> J
    I1 --> J
    J --> K[adr-generator-skills]
    J --> L[c4-diagram-generator-skills]
    K --> M[Generate final markdown report]
    L --> M
```

## Invocation Pattern

Use this contract when the review needs:

- structural analysis
- domain modeling review
- resilience and fault tolerance review
- scalability and performance review
- API governance review
- observability and operability review

## Output Contract

The generated report includes:

- Executive Summary
- 6-Pillar Scorecard
- Critical Findings
- Architecture Smells
- Refactoring Recommendations
- C4 Diagrams
- Architecture Decision Records (ADRs)
- Technical Debt Roadmap

## Presentation Note

Think of the JSON as the stable execution contract for the orchestrator. It is concise, deterministic, and intended to remain the source definition behind the markdown agent layer.
