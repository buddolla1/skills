---
name: skills1
description: Master index for the skills in this repository. Use when you need to choose, combine, or route to the right skill for Java, Spring Boot, React accessibility, testing, performance, documentation, validation, or code quality work.
---

# Skills Index

Use this file as the top-level guide for selecting the right skill in this repository.

## When to Use This Skill

Use this skill when you need a single entry point to discover the available skills, understand what each one does, and route the task to the right specialized skill. If the task spans multiple concerns, pick the narrowest matching skill or combine the relevant ones.

## Prerequisites

- The user request or codebase area to work on
- A clear understanding of the desired outcome
- The relevant repository context if the task is code-related

## Step-by-Step Workflows

1. Identify the primary task domain.
2. Select the most specific matching skill from the catalog below.
3. If the request spans multiple domains, combine the relevant skills in sequence.
4. If no skill clearly fits, ask a clarifying question before acting.
5. Prefer the narrowest skill that solves the problem without overreaching.

## Skill Catalog

### Code Quality & Standards

- [java-code-quality-analyzer](java-code-quality-analyzer/SKILL.md): Detects code smells, long methods, duplicate logic, and maintainability risks in Java.
- [secrets-management-checker](secrets-management-checker/SKILL.md): Flags hardcoded secrets and recommends Vault or environment-based secret handling.
- [java-docs](java-docs/SKILL.md): Documents Java types with Javadoc best practices.
- [sql-code-review](sql-code-review/SKILL.md): Reviews SQL for security, maintainability, and code quality issues.
- [jpa-jdbc-performance-optimizer](jpa-jdbc-performance-optimizer/SKILL.md): Finds N+1 queries, lazy loading issues, and poor fetch strategies in JPA/JDBC code.
- [query-optimizer](query-optimizer/SKILL.md): Improves SQL performance and index usage.
- [sql-optimization](sql-optimization/SKILL.md): Optimizes SQL queries and indexing strategy.
- [stored-procedure-function-explainer](stored-procedure-function-explainer/SKILL.md): Explains stored procedures and functions for Oracle or MySQL.
- [projection-creation](projection-creation/SKILL.md): Creates JPA or JDBC projection/read-model guidance for narrow read paths.
- [yaml-validator](yaml-validator/SKILL.md): Validates YAML structure and calls out URLs ending in `/`.

### Testing

- [unit-test-generator](unit-test-generator/SKILL.md): Generates JUnit and Mockito unit tests with behavior-focused coverage.
- [java-junit](java-junit/SKILL.md): Provides JUnit 5 unit testing best practices.
- [integration-test-builder](integration-test-builder/SKILL.md): Builds `@SpringBootTest` and Testcontainers integration tests.
- [spring-boot-testing](spring-boot-testing/SKILL.md): Selects the right Spring Boot testing technique.
- [javascript-typescript-jest](javascript-typescript-jest/SKILL.md): Writes and reviews JavaScript and TypeScript tests using Jest.
- [react-test-generator](react-test-generator/SKILL.md): Generates tests for React applications.
- [test-coverage-analyzer](test-coverage-analyzer/SKILL.md): Flags low coverage areas and missing tests.
- [threading-async-analyzer](threading-async-analyzer/SKILL.md): Detects blocking calls and suggests `@Async` or `CompletableFuture`.

### Performance & Resilience

- [performance-profiler](performance-profiler/SKILL.md): Identifies bottlenecks and suggests caching or async processing.
- [resilience-patterns-enforcer](resilience-patterns-enforcer/SKILL.md): Adds circuit breaker, retry, and bulkhead guidance using Resilience4j.
- [event-driven-architecture](event-driven-architecture/SKILL.md): Adds Kafka and RabbitMQ patterns for event-driven systems.
- [java-add-graalvm-native-image-support](java-add-graalvm-native-image-support/SKILL.md): Adds GraalVM native image support to Java applications.

### Spring Boot & Modernization

- [spring-3x-to-4x-modernization](spring-3x-to-4x-modernization/SKILL.md): Modernizes Spring Framework 3.x applications to Spring Framework 4.x while improving structure safely.
- [java-springboot](java-springboot/SKILL.md): Applies Spring Boot best practices for Java applications.
- [create-spring-boot-java-project](create-spring-boot-java-project/SKILL.md): Creates a Spring Boot Java project skeleton.
- [springboot-exception-orchestrator](springboot-exception-orchestrator/SKILL.md): Orchestrates exception-risk analysis across large Spring Boot codebases.
- [openapi-swagger-generator](openapi-swagger-generator/SKILL.md): Generates API docs and checks contract consistency.
- [feature-flag-manager](feature-flag-manager/SKILL.md): Manages LaunchDarkly or config-based feature toggles.
- [logging-observability-enhancer](logging-observability-enhancer/SKILL.md): Enforces structured logging and correlation IDs.

### Architecture & Documentation

- [architecture-doc-generator](architecture-doc-generator/SKILL.md): Generates README files, architecture docs, and ADRs.
- [create-readme](create-readme/SKILL.md): Creates or updates project README files.
- [create-specification](create-specification/SKILL.md): Creates implementation-ready specification files.
- [create-technical-spike](create-technical-spike/SKILL.md): Creates time-boxed technical spike documents.
- [acquire-codebase-knowledge](acquire-codebase-knowledge/SKILL.md): Maps a codebase before making changes.

### React Accessibility

- [react-ada-analysis](react-ada-analysis/SKILL.md): Analyzes React projects for ADA accessibility issues.
- [ada-report-codebase-auditor](ada-report-codebase-auditor/SKILL.md): Reconciles ADA `.docx` reports against a React codebase and asks before fixing.
- [react-redux-axios-css-javascript](react-redux-axios-css-javascript/SKILL.md): Builds and reviews React JavaScript projects that use Redux, Axios, and CSS.
- [react-redux-axios-css-typescript](react-redux-axios-css-typescript/SKILL.md): Builds and reviews React TypeScript projects that use Redux, Axios, and CSS.

### Orchestration and Utilities

- [make-skill-template](make-skill-template/SKILL.md): Meta-skill for creating and scaffolding new skills.

## Guardrails

- Do not use a broader skill when a narrower one matches the task better.
- Do not invent behavior that is not covered by the selected skill.
- Do not skip clarification when the request could reasonably map to multiple skills.

## Troubleshooting

- If the task is mostly about code quality, start with the relevant analyzer skill.
- If the task is mostly about testing, start with the test generator or coverage analyzer.
- If the task is about Spring Boot migration or reliability, use the Spring-focused skills first.
- If the task is about React accessibility, use the React ADA skills first.

## References

- The individual `SKILL.md` files in each skill directory
- The `make-skill-template/SKILL.md` standard
