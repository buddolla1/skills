# React ADA Accessibility Analyzer - Agent View

This view summarizes how `react-ada-analyze` should behave in practice.

## Agent Overview

- Input: React `JSX/TSX`, optional ARC-style context via `pageUrl`, `pageUrls`, `domain`, `userFlows`, `projectFiles`, entry points, routes, and design system files.
- Goal: Detect accessibility risks, separate automated findings from manual findings, and provide practical remediation guidance.
- Output: Summary, automated findings, manual findings, user-flow findings, score, recommendations, risk summary, and a professional consolidated report.

## Main Workflow

```mermaid
flowchart TD
  A[Start: Ask user for ARC assessment scope] --> B{Single page, user flow, domain, or full codebase?}
  B -- Single page --> C[Analyze fileContent and pageUrl]
  B -- User flow --> D[Analyze pageUrls and userFlows]
  B -- Domain --> E[Analyze domain, page groups, and projectFiles]
  B -- Full codebase --> F[Analyze projectFiles with entry points, routes, and design system files]
  C --> G[Parse JSX and build AST]
  D --> G
  E --> G
  F --> G
  G --> H[Load ARC context and app structure]
  H --> I[Run automated WCAG checks]
  I --> J[Run manual accessibility and user-flow checks]
  J --> K[Classify severity, confidence, priority, and impact]
  K --> L[Separate automated findings from manual findings]
  L --> M[Calculate accessibility score]
  M --> N[Assemble professional consolidated report]
  N --> O[Generate summary, findings, risk summary, and report object]
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
- Treat page, flow, and domain scope as first-class ARC concepts.
- Call out keyboard, focus, screen reader, contrast, reflow, live region, and motion concerns.
- Distinguish between code-level defects and runtime behavior that needs manual testing.
- Do not claim ADA compliance certification from static analysis alone.
- Separate automated findings, manual findings, and user-flow findings in the final report.

## Preferred Prompts

- What do you want me to analyze?
- What ARC assessment scope should I use?
- Do you want a quick scan or deep accessibility audit?
- Should I include manual test cases for screen reader and keyboard verification?
- Do you want WCAG reference links in the report?

## Expected Output Shape

```mermaid
flowchart LR
  A[assessmentScope] --> B[summary]
  B --> C[automatedFindings]
  C --> D[manualFindings]
  D --> E[userFlowFindings]
  E --> F[score]
  F --> G[recommendations]
  G --> H[manualChecks]
  G --> I[riskSummary]
  I --> J[report]
```
