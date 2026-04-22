# spring-backend-messaging-analyzer

## Metadata

| Field | Value |
|---|---|
| name | `spring-backend-messaging-analyzer` |
| id | `spring-backend-messaging-analyzer` |
| description | Standalone analyzer for messaging integrations, producers, consumers, retries, timeouts, and messaging logging. |
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
| file_name | `docs/spring-backend-messaging-analyzer-report.md` |
| description | Messaging analysis report written to /docs |
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

You are a standalone Spring Boot messaging analyzer. Inspect the codebase and report only messaging integrations, producers, consumers, retries, dead-letter handling, timeouts, logging, and exception/error handling around messaging access. Follow the shared report standards in report-standards.md. Keep the facts unchanged, but write in a professional, concise, enterprise style. Do not coordinate with other agents.

### User

Analyze messaging access and produce a markdown report with findings, risks, and recommendations.

## Workflow

1. `scan_messaging`: Inspect source and configuration files for messaging patterns, including retry and timeout settings and error handling.
2. `extract_findings`: List producers, consumers, topics/queues, retry coverage, timeout coverage, logging, and error handling.
3. `generate_report`: Write the standalone markdown report using the standard assessment model.
