---
name: java-add-graalvm-native-image-support
description: Add GraalVM Native Image support to Java applications. Use when building or fixing native-image compilation, startup performance, or native compatibility issues.
---

# Java Add GraalVM Native Image Support

Use this skill when a Java application needs GraalVM native image support.

## When to Use This Skill

Use this skill when the user asks to enable, build, or troubleshoot native-image support.

## Prerequisites

- The Java project being converted
- The GraalVM and build tool versions
- The runtime features the application depends on

## Goal

Make the project compile and run as a GraalVM native image with minimal friction.

## Step-by-Step Workflows

1. Inspect reflection, proxies, resources, and dynamic class loading.
2. Identify native-image blockers.
3. Update the build and runtime configuration.
4. Build and test the native image.
5. Iterate until the application starts and behaves correctly.

## Guardrails

- Do not assume reflection works without configuration.
- Do not ignore resource loading or proxy requirements.
- Do not claim success without a real native build.

## Output Standard

For each change, provide:

- Native-image issue
- Cause
- Fix applied
- Validation result

## Reporting Style

- Be precise about build failures.
- Prefer targeted fixes.
- Explain any runtime limitation.

## Troubleshooting

- If the image fails to build, inspect reflection and resource usage first.
- If startup fails, verify runtime hints and configuration.
- If a dependency is incompatible, call it out explicitly.

## References

- GraalVM native-image documentation
- Project build and runtime conventions

