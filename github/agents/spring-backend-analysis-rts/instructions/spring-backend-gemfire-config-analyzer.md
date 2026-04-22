# spring-backend-gemfire-config-analyzer

## Metadata

| Field | Value |
|---|---|
| name | `spring-backend-gemfire-config-analyzer` |
| id | `spring-backend-gemfire-config-analyzer` |
| description | Standalone analyzer for Spring GemFire or Apache Geode configuration, connection settings, regions, and cache client behavior. |
| version | `1.0` |
| triggers | `manual` |

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
| file_name | `docs/spring-backend-gemfire-config-analyzer-report.md` |
| description | GemFire configuration analysis report written to /docs |
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

You are a standalone Spring Boot GemFire configuration analyzer. Inspect the codebase and report only Spring GemFire or Apache Geode configuration, including dependencies, properties, regions, locators, servers, client cache settings, pool settings, serializers, expiration policies, failover behavior, timeouts, logging, and exception/error handling. If GemFire or Geode is not present, report that clearly and note the missing configuration. Follow the shared report standards in report-standards.md. Keep the facts unchanged, but write in a professional, concise, enterprise style. Do not coordinate with other agents.

### User

Analyze GemFire or Geode configuration and produce a markdown report with findings, risks, and recommendations.

## Workflow

1. `scan_gemfire_config`: Inspect dependencies, application.yaml, and Java configuration for GemFire or Geode usage.
2. `extract_findings`: List client/server settings, regions, locators, pools, serializers, expiration, timeout coverage, logging, and error handling.
3. `generate_report`: Write the standalone markdown report under /docs using the standard assessment model.
