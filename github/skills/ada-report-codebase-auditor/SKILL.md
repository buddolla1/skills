---
name: ada-report-codebase-auditor
description: Analyze ADA accessibility reports in .docx format and reconcile them against a React codebase. Use when you need to extract accessibility findings from a Word report, verify the issues in code, and ask the user whether they want the fixes applied.
---

# ADA Report Codebase Auditor

Use this skill when an accessibility report arrives as a `.docx` file and the codebase must be checked against those findings.

## When to Use This Skill

Use this skill when the task is to read an ADA accessibility report, compare each item to the React codebase, and produce a verified list of issues. If the project does not have the packages or tooling required to inspect the `.docx` report, prompt the user to add them before continuing.

## Prerequisites

- The ADA report in `.docx` format
- The codebase to validate against the report
- Any document-parsing or accessibility tooling already available in the project

## Goal

Turn a Word-based ADA report into verified code findings, then ask the user whether they want the issues fixed.

## What to Analyze

- Accessibility issues listed in the report
- React components, pages, forms, and navigation flows
- Semantic HTML, keyboard behavior, ARIA usage, and focus handling
- Missing or incorrect accessibility tooling in the project
- Whether the reported issue is actually present in the codebase

## Step-by-Step Workflows

1. Open and extract the ADA findings from the `.docx` report.
2. Identify the relevant code paths, components, or pages for each finding.
3. Verify whether the issue exists in the codebase or is already resolved.
4. Consolidate duplicate or overlapping findings into a single verified issue list.
5. Present the verified issues to the user and ask whether they want the fixes applied.

## Package Check Rule

- If the project lacks the packages needed to parse the `.docx` report or run accessibility checks, prompt the user to add them.
- Do not assume the project can inspect the report until the required tooling is available.
- If accessibility tooling is missing, call that out before attempting automated validation.

## Guardrails

- Do not treat every report item as a confirmed defect without checking the codebase.
- Do not apply fixes before the user confirms they want them.
- Do not hide uncertainty when the report and codebase do not clearly match.
- Prefer verified findings over broad, unconfirmed assumptions.

## Output Standard

For each verified issue, provide:

- Report item
- Code location or component
- Verification result
- Why it matters
- Recommended fix
- Whether user approval is needed before applying changes

## Reporting Style

- Be factual and concise.
- Separate verified issues from report-only claims.
- End the review by asking the user whether they want the fixes applied.

## Troubleshooting

- If the `.docx` report cannot be parsed, ask the user to add the required document-processing package.
- If a reported issue cannot be found in code, mark it as unverified and explain why.
- If the codebase already addresses the issue, note that the report is stale or outdated.

## References

- Accessibility review standards
- Project accessibility tooling and component patterns

