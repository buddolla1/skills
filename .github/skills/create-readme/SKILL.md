---
name: create-readme
description: Create or update a README.md file for a project. Use when documenting setup, usage, configuration, development workflow, or project overview for a repository.
---

# Create README

Use this skill when the task is to write a practical repository README.

## When to Use This Skill

Use this skill when the user asks for a README, wants to refresh project documentation, or needs a clear top-level guide for a repo.

## Prerequisites

- The project purpose and audience
- The setup and run steps
- Any environment or configuration requirements

## Goal

Write a README that helps developers understand, install, run, and contribute to the project.

## Step-by-Step Workflows

1. Identify the audience and the main use case.
2. Gather setup, configuration, and execution steps from the codebase.
3. Write the overview, installation, usage, and troubleshooting sections.
4. Include only the commands and facts that are actually correct for the project.
5. Review the README for clarity and maintenance cost.

## Guardrails

- Do not invent commands or workflows that are not in the repository.
- Do not overload the README with internal design detail.
- Do not hide prerequisites or required environment setup.

## Output Standard

For each README, provide:

- Audience
- Project purpose
- Setup steps
- Usage steps
- Troubleshooting notes

## Reporting Style

- Be concise and practical.
- Prefer commands over prose when instructions matter.
- Keep the top section easy to scan.

## Troubleshooting

- If setup is unclear, inspect build and run scripts first.
- If the README is too long, split architecture details into a separate doc.
- If commands differ by environment, call that out explicitly.

## References

- Existing repository files and scripts
- Project configuration and build tooling

