# React ADA Accessibility Analyzer - Agent View

This view summarizes how `react-ada-analyze` should behave in practice.

## Agent Overview

- Input: React `JSX/TSX`, optional full codebase context via `projectFiles`, plus component purpose, entry points, routes, interaction type, and focus areas.
- Goal: Detect accessibility risks, separate static findings from manual checks, and provide practical remediation guidance.
- Output: Summary, issues, score, recommendations, manual checks, risk summary, and a professional consolidated report.

## Main Workflow

```mermaid
flowchart TD
  A[Start: Ask user for analysis scope] --> B{Selected file or full codebase?}
  B -- Selected file --> C[Analyze fileContent]
  B -- Full codebase --> D[Analyze projectFiles with entry points, routes, and design system files]
  C --> E[Parse JSX and build AST]
  D --> E
  E --> F[Apply WCAG 2.1 and relevant WCAG 2.2 checks]
  F --> G[Scan focus areas]
  G --> H[Detect accessibility violations]
  H --> I[Classify severity, confidence, priority, and impact]
  I --> J[Separate static findings from manual verification needs]
  J --> K[Calculate accessibility score]
  K --> L[Assemble professional consolidated report]
  L --> M[Generate summary, recommendations, manual checks, risk summary, and report object]
```

## Analysis Decision Flow

```mermaid
flowchart TD
  A[Observed pattern] --> B{Is the issue provable statically?}
  B -- Yes --> C[Record issue with WCAG reference]
  B -- No --> D[Mark manualVerificationNeeded = true]
  D --> E[Add manual test steps]
  C --> F{Is the issue high impact?}
  E --> F
  F -- Yes --> G[Raise severity and priority]
  F -- No --> H[Keep severity aligned to user impact]
  G --> I[Include remediation suggestion and example fix]
  H --> I
```

## Practical Rules

- Prefer precision over noise.
- Use semantic HTML before ARIA where possible.
- Use repository context when available to identify cross-page, shared-component, and route-level issues.
- Call out keyboard, focus, screen reader, contrast, reflow, live region, and motion concerns.
- Distinguish between code-level defects and runtime behavior that needs manual testing.
- Do not claim ADA compliance certification from static analysis alone.

## Preferred Prompts

- What do you want me to analyze?
- Do you want a quick scan or deep accessibility audit?
- Should I include manual test cases for screen reader and keyboard verification?
- Do you want WCAG reference links in the report?

## Expected Output Shape

```mermaid
flowchart LR
  A[analysisMode] --> B[summary]
  B --> C[issues]
  C --> D[score]
  D --> E[recommendations]
  E --> F[manualChecks]
  E --> G[riskSummary]
  G --> H[report]
```
