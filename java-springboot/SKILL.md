---
name: java-springboot
description: Apply Spring Boot best practices for Java applications. Use when reviewing or creating Spring Boot code for configuration, dependency injection, controllers, services, data access, logging, testing, and security.
---

# Java Spring Boot

Use this skill when working on Spring Boot Java applications and you want standard, production-friendly guidance.

## When to Use This Skill

Use this skill when the task involves Spring Boot application design, code review, or implementation guidance.

## Prerequisites

- The application area being worked on
- The Java and Spring Boot versions if they matter
- The behavior the user wants to preserve or improve

## Goal

Help produce maintainable Spring Boot code that follows common best practices.

## Step-by-Step Workflows

1. Check the project structure and dependencies.
2. Review configuration, dependency injection, web, service, and data layers.
3. Verify logging, testing, and security conventions.
4. Point out missing or risky Spring Boot patterns.
5. Recommend the smallest safe improvement.

## Guardrails

- Do not expose entities directly when DTOs are better.
- Do not hardcode configuration or secrets.
- Do not scatter business logic across controllers.

## Output Standard

For each issue, provide:

- Layer or component
- Best-practice gap
- Why it matters
- Recommended fix

## Reporting Style

- Be concise and practical.
- Prefer established Spring Boot conventions.
- Tie advice to maintainability and testability.

## Troubleshooting

- If the version is unclear, inspect build metadata first.
- If a layer is overloaded, suggest a better separation of concerns.
- If configuration is mixed with code, externalize it.

## References

- Spring Boot conventions
- Project-specific coding standards

