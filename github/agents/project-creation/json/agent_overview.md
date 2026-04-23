# Project Creation Agent Overview

## Overview

This folder contains the machine-readable contract and instruction file for the `springboot-starter-project` agent.

## Files

- [`springboot-starter-project.json`](springboot-starter-project.json)
- [`springboot-starter-project.md`](../instructions/springboot-starter-project.md)

## Flow Chart

```mermaid
flowchart TD
    A[Load project-creation contract] --> B[Read JSON and instructions]
    B --> C[Resolve springboot-starter-project]
    C --> D[Gather project type and feature choices]
    D --> E[Generate project structure]
    E --> F[Add build, config, security, and JDBC scaffolding]
    F --> G[Add tests and documentation]
    G --> H[Return starter project output]
```

## Purpose

The agent generates a production-ready Spring Boot starter project with:
- REST controllers
- JDBC or `JdbcTemplate` data access
- Spring Security baseline configuration
- JUnit 5 and Mockito testing setup
- `application.yml` and properties templates

## Typical Uses

- scaffold a new Spring Boot service
- standardize a single-module project
- generate a multi-module project layout
- add starter build and configuration templates

## Example Prompt

- `@springboot-starter-project projectType=single features=rest,jdbc,testing`
