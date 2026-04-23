# Skills Overview

## Executive Summary

Agent Skills are a portable, open format for adding specialized capabilities, workflows, and reference material to AI agents on demand.

Each skill is a self-contained directory centered on `SKILL.md`. The file defines the skill’s purpose, when it should activate, and how the agent should execute it. Supporting scripts, templates, and references can sit alongside it.

## Skill Structure

```text
skill-name/
├── SKILL.md          # Required: metadata and instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: supporting documentation
├── assets/           # Optional: templates, images, schemas
└── ...               # Additional files if needed
```

## How Skills Work

Skills follow progressive disclosure:

1. Discovery: the agent loads only the skill name and description.
2. Activation: when the task matches, the agent loads the full `SKILL.md`.
3. Execution: the agent follows the instructions and loads supporting files only when needed.

This keeps the base context lean while preserving access to deeper expertise when required.

## Why Skills Matter

- Clear intent: the same `SKILL.md` is readable by both humans and agents.
- Better reuse: one skill can support many tasks, conversations, and agents.
- Portable design: skills are plain files that are easy to share and version.
- Extensible delivery: a skill can include code, examples, and reference material.
- Consistent execution: skills make complex work easier to repeat and audit.

## How To Use Skills

Start with the skill name and description to confirm it matches the task. If it does, open the full `SKILL.md`, follow the workflow, and load supporting files only when the instructions reference them.

When a skill provides scripts or templates, reuse them instead of rebuilding the process manually.

## Skills vs Custom Instructions

| Area | Agent Skills | Custom Instructions |
|---|---|---|
| Purpose | Specialized capabilities and workflows | Standards, conventions, and guidelines |
| Content | Instructions, scripts, examples, resources | Instructions only |
| Scope | Task-specific and loaded on demand | Usually always applied |
| Portability | Open standard across compatible agents | More tool-specific |

Use skills for reusable capabilities. Use custom instructions for project rules, coding conventions, and review preferences.

## VS Code Considerations

VS Code can discover skills in project and personal locations such as `.github/skills/`, `.claude/skills/`, and `.agents/skills/`, plus the matching user-level paths.

Skills can also surface as slash commands in chat. Frontmatter fields like `user-invocable` and `disable-model-invocation` control whether a skill is visible in the menu or loaded automatically.

## Specification Highlights

The Agent Skills specification defines a skill as a directory containing `SKILL.md`, with optional `scripts/`, `references/`, and `assets/` folders.

`SKILL.md` uses YAML frontmatter followed by Markdown body content. Key fields include:

- `name`: lowercase identifier that matches the parent directory name
- `description`: what the skill does and when to use it
- `license`: optional license information
- `compatibility`: optional environment requirements
- `metadata`: optional key-value data
- `allowed-tools`: optional pre-approved tools

Recommended operating principles:

- Keep the main `SKILL.md` under 500 lines.
- Load supporting files only when needed.
- Validate skills with the reference library.

### Using Scripts

Skills can instruct agents to run shell commands and bundle reusable scripts in a scripts/ directory
 
Script guidance:

npx runs npm packages, downloading them on demand. It ships with npm (which ships with Node.js).
npx eslint@9 --fix .
npx create-vite@6 my-app
Bundled with Node.js — no extra install needed.
Downloads the package, runs it, and caches it for future use.
Pin versions with npx package@version for reproducibility.

Use relative paths from the skill directory root to reference bundled files. The agent resolves these paths automatically — no absolute paths needed.
List available scripts in your SKILL.md so the agent knows they exist:
List available scripts in your SKILL.md so the agent knows they exist:
### Naming Examples

Valid names:

- `pdf-processing`
- `data-analysis`
- `code-review`

Invalid names:

- `PDF-Processing`
- `-pdf`
- `pdf--processing`

### Description Examples

Good description:

- `Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.`

Poor description:

- `Helps with PDFs.`

### Assets Examples

The `assets/` directory is for static resources such as templates, diagrams, images, lookup tables, and schemas.

Valid examples:

- `assets/report-template.md`
- `assets/architecture-diagram.png`
- `assets/field-map.json`

Invalid examples:

- `assets/README.txt` when used as detailed reference text instead of a static asset
- `assets/scripts/extract.py` because executable code belongs in `scripts/`
- `assets/references/spec.md` because documentation belongs in `references/`

### References

The `references/` directory stores supporting documentation, rules, or checklists that the agent reads when it needs deeper guidance.

## Repository Context

In this repository, the top-level `SKILL.md` is the index for available skills. Each folder contains a specialized skill for areas such as documentation, testing, Java, Spring Boot, React, SQL, and validation.

## Key Takeaways

- Skills package expertise into a reusable format.
- Progressive disclosure keeps agent context efficient.
- `SKILL.md` is the core contract for each skill.
- Scripts, references, and assets extend the skill without cluttering the main instructions.

## Sources

- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Specification](https://agentskills.io/specification)
- [What are skills?](https://agentskills.io/what-are-skills)
