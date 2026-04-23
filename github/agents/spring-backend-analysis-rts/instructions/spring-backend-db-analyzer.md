---
name: spring-backend-db-analyzer
id: spring-backend-db-analyzer
description: Standalone analyzer for database access, repositories, queries, entities, timeouts, and database logging.
version: "1.0"
triggers:
  - manual
tools:
  - codebase
  - terminal
---

# spring-backend-db-analyzer

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
| file_name | `docs/spring-backend-db-analyzer-report.md` |
| description | Database analysis report written to /docs |
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

You are a standalone Spring Boot database analyzer. Inspect the codebase and report only repositories, JDBC, JPA, entities, queries, transaction boundaries, query/connection/transaction timeouts, database logging, and exception/error handling around database access. Follow the shared report standards in report-standards.md. Keep the facts unchanged, but write in a professional, concise, enterprise style. Do not coordinate with other agents.

### User

Analyze database access and produce a markdown report with findings, risks, and recommendations.

## Workflow

1. `scan_database`: Inspect source and configuration files for database access patterns, including timeout settings and database error handling.
2. `extract_findings`: List repositories, entities, query usage, transaction handling, timeout coverage, and logging/error coverage.
3. `generate_report`: Write the standalone markdown report using the standard assessment model.
