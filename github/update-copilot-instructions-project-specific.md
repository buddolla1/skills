# Update Copilot Instructions for This Project

Use this prompt when you want Copilot instructions rewritten to match the existing project instead of a generic template.

## Why This Helps

1. It keeps the instructions aligned with the real project structure instead of a generic Spring Boot layout.
2. It reduces incorrect guidance caused by assumptions about packages, layers, or persistence choices.
3. It improves consistency across controllers, services, repositories, DTOs, and other project boundaries.
4. It makes future updates easier because the instructions reflect the codebase that already exists.
5. It helps Copilot produce output that is more accurate, maintainable, and specific to this project.

```text
Update the repository Copilot instructions so they match my existing project structure and architecture.

Task:
- Inspect the current codebase and infer the real package layout, module boundaries, naming conventions, and architecture patterns already in use.
- Compare the existing project structure against the current instruction file.
- Rewrite the instructions so they describe my project accurately, not a generic Spring Boot template.
- Remove assumptions that do not match the codebase.
- Preserve the existing intent of the instructions, but make them project-specific.

What to update:
- Actual root package name and package hierarchy
- Real layer names and boundaries used in the project
- Whether the project uses layered, clean, hexagonal, modular monolith, or another style
- Existing conventions for controllers, services, repositories, DTOs, entities, mappers, exceptions, config, clients, security, tests, and utilities
- Actual persistence strategy used in the project
- Existing API style, validation, exception handling, and response conventions
- Existing build tool, modules, and test setup if relevant

Rules:
- Do not invent structure that is not present in the codebase.
- Keep behavior-preserving guidance.
- Do not recommend architectural refactors unless the codebase already uses them.
- Prefer concise, clear instructions over generic best-practice lists.
- Keep links to topic files if they still make sense.
- If a rule conflicts with the project’s real structure, update the instruction to match the project.

Output:
- Return only the revised instruction content.
- Make it ready to paste into `copilot-instructions.md`.
```
