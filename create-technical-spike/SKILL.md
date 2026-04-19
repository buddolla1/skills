---
name: create-technical-spike
description: Create a time-boxed technical spike document for research, validation, and decision support. Use when investigating risks, unknowns, package choices, feasibility, or design alternatives before implementation.
---

# Create Technical Spike

Use this skill when a short research phase is needed before building or changing a system.

## When to Use This Skill

Use this skill when the user wants to explore an option, prove feasibility, compare approaches, or reduce uncertainty before committing to implementation.

## Prerequisites

- The question being investigated
- The options being compared
- The time or scope boundary for the spike

## Goal

Produce a focused spike document that answers a specific technical question and leads to a decision.

## Step-by-Step Workflows

1. State the question and the reason it matters.
2. Define the options or experiments to compare.
3. Set the time box and success criteria.
4. Capture findings, risks, and recommendation.
5. Record the decision and the next action.

## Guardrails

- Do not let a spike become open-ended research.
- Do not bury the recommendation in analysis.
- Do not confuse a spike with an implementation plan.

## Output Standard

For each spike, provide:

- Question
- Options considered
- Findings
- Recommendation
- Follow-up action

## Output Location

- Write generated spike documents to the repository `doc/` folder unless the user explicitly requests a different path.
- Create `doc/` first if it does not exist.

## Reporting Style

- Be time-boxed and decision-oriented.
- Prefer evidence over opinion.
- Keep the conclusion easy to act on.

## Troubleshooting

- If the question is too broad, narrow it to one decision.
- If the spike produces no decision, clarify what outcome is needed.
- If the research needs more depth, split it into phases.

## References

- Related specifications and ADRs
- Existing architecture notes
