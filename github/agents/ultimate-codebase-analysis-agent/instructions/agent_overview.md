# Ultimate Codebase Analysis Agent - Overview

## Overview

This agent orchestrates large-codebase analysis by splitting work across specialized internal analyzers and consolidating the results into a single markdown report.

It is designed for:
- full repository review
- git diff review
- Java and Spring backend analysis
- dependency review
- exception and runtime-risk review
- instruction compliance verification

## Supported Workflow

1. Scan the repository and build a module/file map.
2. Run analysis agents in parallel.
3. Verify compliance against instruction-based rules.
4. Generate one final markdown report.

## Architecture Overview

The architecture is optimized for large repositories by:
- chunking by module
- using a minimum of 6 agents and a maximum of 9 agents
- limiting work per agent
- using parallel execution for independent analysis
- aggregating outputs into a single reporter stage

```mermaid
flowchart TD
    A[Start] --> B[Select scan mode]
    B --> C{Scan mode}
    C -->|full| D[Scan entire repository]
    C -->|diff| E[Scan changed files only]
    D --> F[Build file and module map]
    E --> F
    F --> G{scanMode}
    G -->|full| H[Run static, exception, dependency, and performance analysis]
    G -->|diff| I[Run static and exception analysis only]
    H --> J[Aggregate findings]
    I --> J
    J --> K{Instruction file present?}
    K -->|Yes| L[Instruction compliance verifier]
    K -->|No| M[Reporter]
    L --> M
    M --> N[Write markdown report]
```

## Agents and Responsibilities

- Scanner: discover repository structure and prepare analysis scope
- Static Analyzer: detect defects, anti-patterns, and performance issues
- Exception Analyzer: review exception handling quality and runtime failure modes
- Dependency Analyzer: review build and dependency health
- Performance Analyzer: review hot paths, allocation pressure, database access, caching, and concurrency bottlenecks
- Instruction Compliance Verifier: enforce rules from the instruction source
- Reporter: generate the final executive report

## Agent Count Rule

- Minimum agents: 6
- Maximum agents: 9
- Keep the core scanner, analyzers, compliance verifier, and reporter in place
- Add optional specialist agents only when the review scope justifies them
- Select `full` or `diff` scan mode before scanning begins
- `full` runs dependency and performance analysis; `diff` skips both

## How To Use

- `@ultimate-codebase-analysis-agent`
- `@ultimate-codebase-analysis-agent scanMode=full`
- `@ultimate-codebase-analysis-agent scanMode=diff`
- `@ultimate-codebase-analysis-agent performance-analysis`
- `@ultimate-codebase-analysis-agent summarize critical issues`
- `@ultimate-codebase-analysis-agent scan module portal`

## Output

The final report is written as `codebase-analysis-report.md` and includes:
- Summary
- Critical Issues
- High Issues
- Medium Issues
- Low Issues
- Exception Highlights
- Dependency Risks
- Performance Highlights
- Compliance Summary
- Compliance Violations
- Recommendations

## Best Practice

Use full scan for baseline audits and diff scan for pull requests or targeted validation. Keep compliance verification enabled for every run that has an instruction source.

## Note

This agent does not use a separate `Skills` section. Its operational capabilities are expressed through:
- agents and responsibilities
- execution strategy
- workflow steps
- compliance enforcement rules
- compliance verification runs only when an instruction file is present
