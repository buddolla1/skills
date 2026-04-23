# Architecture Baseline Before Copilot Update

Use this prompt when you want to review the existing project architecture first, then update Copilot instructions to match the real codebase.

## Why This Matters

For an existing project, a baseline-first approach keeps the instructions grounded in the real codebase instead of a generic template.

This is helpful because it:

1. Aligns Copilot instructions with the actual project architecture.
2. Reduces incorrect assumptions about packages, layers, and persistence choices.
3. Improves consistency across controllers, services, repositories, DTOs, and supporting code.
4. Makes future instruction updates faster because the architecture has already been documented.
5. Helps Copilot generate output that is more accurate, maintainable, and specific to the project.

```text
Create an architecture baseline for the current project before updating the Copilot instructions.

Goal:
- Analyze the existing project structure and produce a clear architecture baseline first.
- Use that baseline to rewrite the Copilot instructions so they match the actual codebase.

Why:
- The project already exists, so the instructions should be based on real package structure, module boundaries, persistence style, API patterns, and cross-cutting concerns.
- A baseline reduces guesswork and makes the final instructions accurate and project-specific.

Recommended order:
1. Inspect the current codebase.
2. Document the real architecture, package layout, module boundaries, and conventions.
3. Use that baseline to update `copilot-instructions.md`.
4. Re-check the instructions if the codebase changes later.

If the architecture review tooling is available, use it to generate:
- An executive summary
- Key findings
- Package and layer structure
- Persistence and transaction patterns
- API and exception handling conventions
- Security, observability, and testing conventions

Output:
- First provide the architecture baseline.
- Then provide the revised Copilot instructions.
- Keep the final instructions aligned with the actual project, not a generic Spring Boot template.
```
