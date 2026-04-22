# Skill: dependency-patterns

## Purpose
Detect dependency and layering issues.

## When To Use
Use this skill for cross-module wiring, service dependencies, and shared component design.

## Instructions
- Check for cyclic dependencies.
- Check for framework leakage into domain logic.
- Check for over-coupled services and missing interface boundaries.
- Check for risky cross-module dependencies.
- Reuse the architecture guidance from [architecture-and-coding.md](../../../../instructions/topics/architecture-and-coding.md).

## Output
- Dependency issue
- Severity
- File
- Boundary risk
- Recommended fix
