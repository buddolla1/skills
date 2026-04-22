# Skill: performance-patterns

## Purpose
Detect backend performance and scalability issues.

## When To Use
Use this skill for service logic, persistence access, integration code, and hot-path workflows.

## Instructions
- Check for N+1-style access patterns.
- Check for repeated remote calls and chatty service logic.
- Check for blocking I/O in critical paths.
- Check for expensive logging, oversized transactions, and unnecessary in-memory transformations.
- Check for missing pagination or streaming.

## Output
- Performance issue
- Severity
- File
- Why it matters
- Recommended fix
