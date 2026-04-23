# Observability Agents Overview

## Overview

This folder contains observability-focused agents for logging, anomaly detection, and performance review.

## Agents

- [`log-anomaly-detection-agent.md`](../instructions/log-anomaly-detection-agent.md) - scan logs for recurring errors, silent failures, configuration issues, and operational gaps
- [`logging-monitoring-helper.md`](../instructions/logging-monitoring-helper.md) - review logging, MDC, metrics, tracing, and observability hygiene in Spring Boot services
- [`performance-optimizer-helper.md`](../instructions/performance-optimizer-helper.md) - identify Java and Spring Boot performance bottlenecks

## Primary JSON Contracts

- [`log-anomaly-detection-agent.json`](log-anomaly-detection-agent.json)
- [`logging-monitoring-helper.json`](logging-monitoring-helper.json)
- [`performance-optimizer-helper.json`](performance-optimizer-helper.json)

## Typical Uses

- `log-anomaly-detection-agent` for production log analysis and anomaly reports
- `logging-monitoring-helper` for logging quality, metrics, tracing, and MDC checks
- `performance-optimizer-helper` for CPU, memory, database, and concurrency review

## Flow Charts

### `log-anomaly-detection-agent`

```mermaid
flowchart TD
    A[Load log-anomaly-detection-agent.md] --> B[Resolve trigger and prompt]
    B --> C[Choose log source]
    C --> D[Scan logs recursively]
    D --> E[Detect recurring errors]
    D --> F[Detect performance degradation]
    D --> G[Detect silent failures]
    D --> H[Detect configuration issues]
    D --> I[Detect operational gaps]
    E --> J[Classify severity]
    F --> J
    G --> J
    H --> J
    I --> J
    J --> K[Generate markdown or CSV report]
```

### `logging-monitoring-helper`

```mermaid
flowchart TD
    A[Load logging-monitoring-helper.md] --> B[Resolve trigger and prompt]
    B --> C[Select focus area]
    C --> D[Review SLF4J/Logback configuration]
    C --> E[Review metrics instrumentation]
    C --> F[Review tracing and correlation]
    C --> G[Review logging noise and log levels]
    D --> H[Generate markdown report]
    E --> H
    F --> H
    G --> H
```

### `performance-optimizer-helper`

```mermaid
flowchart TD
    A[Load performance-optimizer-helper.md] --> B[Resolve trigger and prompt]
    B --> C[Select analysis type]
    C --> D[Review dependencies and task graph]
    C --> E[Inspect build performance]
    C --> F[Inspect task redundancy]
    D --> G[Generate optimization findings]
    E --> G
    F --> G
```

## Notes

- Reusable skills are not required for this suite.
- Keep the instruction files aligned with the JSON contracts and trigger patterns.
