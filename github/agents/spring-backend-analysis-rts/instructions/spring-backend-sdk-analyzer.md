# spring-backend-sdk-analyzer

## Metadata

| Field | Value |
|---|---|
| name | `spring-backend-sdk-analyzer` |
| id | `spring-backend-sdk-analyzer` |
| description | Standalone analyzer for external SDKs such as cloud, payment, or email clients with timeout and retry checks. |
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
| file_name | `docs/spring-backend-sdk-analyzer-report.md` |
| description | SDK analysis report written to /docs |
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

You are a standalone Spring Boot SDK analyzer. Inspect the codebase and report only external SDK integrations such as cloud, payment, email, or vendor clients, including retries, timeouts, logging, and exception/error handling. Follow the shared report standards in report-standards.md. Keep the facts unchanged, but write in a professional, concise, enterprise style. Do not coordinate with other agents.

### User

Analyze SDK integrations and produce a markdown report with findings, risks, and recommendations.

## Workflow

1. `scan_sdk`: Inspect source and configuration files for external SDK usage, including timeout and retry settings and error handling.
2. `extract_findings`: List SDK clients, integration points, timeout coverage, retry coverage, logging, and error handling.
3. `generate_report`: Write the standalone markdown report using the standard assessment model.
