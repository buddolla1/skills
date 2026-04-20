---
name: spring-boot-testing
description: Select and apply Spring Boot testing techniques. Use when choosing between @SpringBootTest, test slices, Mockito, and Testcontainers for Spring Boot applications.
---

# Spring Boot Testing

Use this skill when choosing the right test strategy for Spring Boot code.

## When to Use This Skill

Use this skill when the task involves Spring Boot testing strategy, test selection, or improving coverage of Spring-based code.

## Prerequisites

- The layer or behavior being tested
- The Spring Boot components involved
- Any existing testing conventions in the project

## Goal

Choose the lightest test type that proves the desired behavior while keeping tests reliable.

## Step-by-Step Workflows

1. Identify the behavior and the Spring layer involved.
2. Choose between unit, slice, or full-context testing.
3. Add Testcontainers when real infrastructure matters.
4. Verify the minimum behavior needed for confidence.
5. Keep the test suite balanced between speed and realism.

## Guardrails

- Do not use full context tests when a slice test is enough.
- Do not over-mock integration behavior.
- Do not pay the cost of containers unless the dependency matters.

## Output Standard

For each test recommendation, provide:

- Test type
- Reason for choosing it
- What it proves
- What it does not prove

## Reporting Style

- Be pragmatic.
- Prefer the smallest test that gives real confidence.
- Tie test choice to the behavior under review.

## Troubleshooting

- If the test is too slow, reduce scope.
- If the test is too fake, move closer to the real dependency.
- If the layer is unclear, map the Spring boundary first.

## References

- Spring Boot testing conventions
- Existing unit and integration test patterns

