# Skill: java-exception-patterns

## Purpose
Detect common Java runtime and exception-handling issues.

## When To Use
Use this skill for service logic, utilities, repositories, mappers, and parsing code.

## Instructions
- Look for null dereference risks.
- Check for unchecked assumptions and unsafe collection access.
- Flag swallowed exceptions and broad `catch (Exception)`.
- Review risky `Optional` usage and unsafe parsing or casting.
- Reuse the defensive-coding guidance from [api-and-exceptions.md](../../../../instructions/topics/api-and-exceptions.md).

## Output
- Runtime risk
- Severity
- File
- Failure explanation
- Recommended fix
