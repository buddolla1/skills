# Skill: risk-prioritizer

## Purpose
Normalize findings into severity and business impact.

## When To Use
Use this skill after a sub-agent has identified concrete issues.

## Instructions
- Classify findings as Critical, High, Medium, or Low.
- Include likelihood, production impact, operability impact, and remediation order.
- Prefer the highest-confidence, highest-impact risk first.
- Downgrade uncertain items to needs-validation instead of overstating them.

## Output
- Severity
- Likelihood
- Production impact
- Operability impact
- Remediation order
