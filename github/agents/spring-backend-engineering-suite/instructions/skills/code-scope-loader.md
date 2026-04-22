# Skill: code-scope-loader

## Purpose
Load the right code scope for Spring backend analysis.

## When To Use
Use this skill at the start of every Spring backend review.

## Instructions
- If `mode=diff-scan`, collect changed files against the provided base branch.
- If `mode=full-scan`, analyze the entire backend source tree.
- Prioritize `src/main/java`, `src/test/java`, `src/main/resources`, build files, and deployment configs.
- Carry the selected scope forward to downstream sub-agents.

## Output
- Scope definition
- Changed files or full scan target
- Files or directories prioritized
