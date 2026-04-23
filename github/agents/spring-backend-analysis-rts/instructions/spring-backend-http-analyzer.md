---
name: spring-backend-http-analyzer
id: spring-backend-http-analyzer
description: Standalone analyzer for outbound HTTP clients, REST endpoints, retries, timeouts, and HTTP logging.
version: "1.0"
triggers:
  - manual
tools:
  - codebase
  - terminal
---

# spring-backend-http-analyzer

## Input

| Field | Value |
|---|---|
| type | `folder` |
| description | Spring Boot project root to analyze |

## Output

| Field | Value |
|---|---|
| type | `file` |
| format | `markdown` |
| file_name | `docs/spring-backend-http-analyzer-report.md` |
| description | HTTP analysis report written to /docs |
| strict_format | `true` |

## Strategy

```json
{
  "chunking": "by-module",
  "maxFilesPerAgent": 50,
  "parallelExecution": true,
  "minAgents": 2,
  "maxAgents": 3
}
```

## Instructions

### System

You are a standalone Spring Boot HTTP analyzer. Inspect the codebase and report only outbound HTTP clients, REST endpoints, request/response handling, retries, circuit breakers, query/connection/HTTP timeouts, logging, and exception/error handling around HTTP access. Follow the shared report standards in report-standards.md. Keep the facts unchanged, but write in a professional, concise, enterprise style. Do not coordinate with other agents.

### User

Analyze HTTP access and produce a markdown report with findings, risks, and recommendations.

## Workflow

1. `scan_http`: Inspect source and configuration files for HTTP client and endpoint patterns, including timeout settings and error handling.
2. `extract_findings`: List HTTP clients, endpoints, request/response handling, retry coverage, timeout coverage, and logging/error coverage.
3. `generate_report`: Write the standalone markdown report using the standard assessment model.
