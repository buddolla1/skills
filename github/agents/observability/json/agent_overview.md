# Observability Agents Overview - JSON

## Overview

This folder contains the machine-readable contracts for the observability agents.

## Agents

- [`log-anomaly-detection-agent.json`](log-anomaly-detection-agent.json) - detect recurring errors, silent failures, performance degradation, and observability gaps in logs
- [`logging-monitoring-helper.json`](logging-monitoring-helper.json) - review logging, MDC, metrics, tracing, and observability hygiene in Spring Boot services
- [`performance-optimizer-helper.json`](performance-optimizer-helper.json) - identify Java and Spring Boot performance bottlenecks

## Purpose

These JSON contracts define the agent identity, prompts, tools, guided interaction, and output behavior for observability-focused analysis.

## Typical Uses

- production log anomaly analysis
- logging and monitoring review
- performance review for Java and Spring Boot services
- observability and incident-readiness checks

## Flow Charts

### `log-anomaly-detection-agent`

```mermaid
flowchart TD
    A[Load log-anomaly-detection-agent.json] --> B[Resolve trigger and prompt]
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
    A[Load logging-monitoring-helper.json] --> B[Resolve trigger and prompt]
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
    A[Load performance-optimizer-helper.json] --> B[Resolve trigger and prompt]
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
- Keep the JSON and instruction files aligned on agent names and trigger patterns.
