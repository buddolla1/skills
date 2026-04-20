# 🧩 Spring Boot Project — Engineering Standards & Best Practices

Use this file as the short entry point for Spring Boot work in this repository.
It replaces the previous `.github/instructions/instructions.md` entry point.
Load the topic files below only when the task needs them.

## Project Context

- Language: Java 21+
- Framework: Spring Boot 3.x+
- API style: REST
- Architecture: layered / clean / hexagonal depending on service needs
- Build tool: Maven or Gradle

## Load On Demand

- [architecture-and-coding.md](instructions/topics/architecture-and-coding.md): structure, layering, coding standards, Java style, and anti-patterns
- [api-and-exceptions.md](instructions/topics/api-and-exceptions.md): REST rules, validation, exception handling, and response contracts
- [data-access.md](instructions/topics/data-access.md): JPA, JDBC, repositories, and transaction management
- [quality-and-ops.md](instructions/topics/quality-and-ops.md): security, performance, testing, logging, build, containerization, CI/CD, documentation, and definition of done

## Usage Rules

- For new code, follow the relevant reference file first.
- For existing code, preserve local file and module patterns.
- For large changes, load only the topic files that match the request.
- Do not load every reference file unless the task is a full repository scan.

## Related Overview

- [copilot-ecosystem.md](copilot-ecosystem.md): full map of agents, skills, hooks, and flow diagrams.
