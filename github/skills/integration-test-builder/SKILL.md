---
name: integration-test-builder
description: Build Spring Boot integration tests with @SpringBootTest and Testcontainers. Use when validating application wiring, repository behavior, REST endpoints, database interactions, messaging, or external dependencies in a production-like test environment.
---

# Integration Test Builder

## When to Use This Skill

Use this skill when writing integration tests that need the real Spring context and external infrastructure.

## Prerequisites

- The application boundary that must be real in the test
- Any containers, profiles, or config overrides needed for setup
- The exact behavior the integration test must prove

## Goal

Verify the application works as an integrated system, not just as isolated units, while keeping the test setup stable and repeatable.

## What to Build

- `@SpringBootTest` based application tests
- Testcontainers-backed dependencies such as databases, brokers, or supporting services
- End-to-end checks for repository, service, and controller wiring
- Configuration-driven test setups that mirror production-like behavior

## Step-by-Step Workflows

1. Identify what must be real: Spring context, database, messaging, or external service.
2. Keep unit-test concerns out of the integration test unless the wiring matters.
3. Ensure the test starts with deterministic container and environment setup.
4. Verify the real behavior the system promises, not internal implementation details.
5. Keep the test scope focused enough to remain fast and reliable in CI.

## Spring Boot Guidance

- Prefer `@SpringBootTest` when the full application context is the behavior under test.
- Use profile-specific properties or test configuration to isolate dependencies.
- Keep bean overrides minimal and explicit.
- Make startup failures visible early so broken wiring does not pass silently.

## Testcontainers Guidance

- Define containers that match the integration dependency the code actually uses.
- Manage lifecycle consistently so tests remain repeatable.
- Prefer reusable container setup patterns for common infrastructure.
- Validate connection properties, schema initialization, and health at startup.

## Coverage Checks

- Application context loads with the intended configuration
- Persistence, messaging, and HTTP wiring function together
- External dependency integration behaves as expected
- Error handling works when a real dependency fails or returns invalid data

## Output Standard

For each integration test set, provide:

- Scenario covered
- Real dependencies exercised
- Configuration used
- Behaviors validated
- Remaining risk or coverage gap

## Reporting Style

- Be explicit about what is integration-level versus unit-level.
- Prefer fewer, high-value integration tests over broad slow suites.
- Call out startup cost, flakiness risk, and dependency assumptions.

## Troubleshooting

- If the test is slow, shrink the scope before adding more containers.
- If the context does not start, make the wiring failure visible early.
- If the test is too mocked, move more of the dependency chain into the real setup.

## References

- Spring Boot test documentation
- Testcontainers setup conventions for the project
