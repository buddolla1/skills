# React ADA Accessibility Fixer - Agent View

This view summarizes how `react-ada-fixer` should behave in practice.

## Agent Overview

- Input: React `JSX/TSX`, optional ARC-style context, a finding or issue description, and component purpose.
- Goal: Apply conservative accessibility fixes without changing product intent.
- Output: Fixed code, diff, explanation, checklist, safety notes, manual verification steps, and an ARC fix summary.

## Main Workflow

```mermaid
flowchart TD
  A[Start: Receive finding or issue] --> B[Load ARC scope and optional multi-file context]
  B --> C[Parse JSX and surrounding context]
  C --> D[Identify accessibility issues]
  D --> E[Check intent, page behavior, and user-flow preservation]
  E --> F{Can the issue be fixed safely?}
  F -- Yes --> G[Prepare smallest correct fix]
  G --> H[Ask user to confirm applying the fix]
  H --> I{User confirmed?}
  I -- Yes --> J[Generate diff and fixed code]
  J --> K[Explain fix and accessibility impact]
  K --> L[Return fixedCode, checklist, manual verification steps, and ARC fix summary]
  I -- No --> M[Return analysis and recommended fix only]
  F -- No --> N[Mark reviewRequired = true]
  N --> O[Provide safest partial fix or recommendation]
  O --> P[Add safety notes and manual verification steps]
  P --> M
```

## Fix Decision Flow

```mermaid
flowchart TD
  A[Observed issue] --> B{Native semantic element available?}
  B -- Yes --> C[Prefer native HTML element]
  B -- No --> D{ARIA is truly needed?}
  D -- Yes --> E[Add minimal valid ARIA]
  D -- No --> F[Keep or refactor structure conservatively]
  C --> G{Behavior preserved?}
  E --> G
  F --> G
  G -- Yes --> H[Return canAutoFix = true and needsConfirmation = true]
  G -- No --> I[Set reviewRequired = true]
  I --> J[Explain ambiguity and request manual review]
```

## Practical Rules

- Prefer semantic HTML before ARIA.
- Do not convert behavior blindly if the control is not actually a button.
- Always preserve keyboard support, focus behavior, and accessible naming.
- Return manual verification steps when static analysis cannot prove runtime behavior.
- Flag ambiguous cases instead of guessing.
- Keep the ARC scope in view so fixes do not break a page, user flow, or domain-level pattern.

## Expected Output Shape

```mermaid
flowchart LR
  A[issuesDetected] --> B[fixedCode]
  B --> C[diff]
  C --> D[explanation]
  D --> E[accessibilityChecklist]
  D --> F[safetyNotes]
  D --> G[manualVerificationSteps]
  G --> H[arcFixSummary]
```
