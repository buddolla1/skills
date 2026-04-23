# Why Skill Files Behave Differently vs Agents with Skills

## 🔹 Core Reason

Skills and agents behave differently because they are:

- Activated differently
- Scoped differently
- Loaded into context differently

---

## 1. Skill = Conditional | Agent = Primary

- A **skill** is loaded only when Copilot decides it is relevant.
- A **custom agent** is the active persona from the start.

📌 Docs:  
https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features

---

## 2. Skills are Additive | Agents are Controlling

- Skills = add extra instructions/tools for a task
- Agents = define behavior, tone, structure, workflow

So:

- Skill → “extra help if needed”
- Agent → “this is the main brain”

📌 Docs:  
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/add-skills

---

## 3. Skill (Direct Call) Feels Raw

When you call a skill directly:

- No strong orchestration
- Relies on current chat context
- Behavior may feel inconsistent

When using an agent:

- Structured flow
- Defined role
- Consistent outputs

📌 Docs:  
https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents

---

## 4. Agents Can Delegate (Skills Cannot)

- Agents can use **subagents** with isolated context
- Skills do NOT create isolated execution

👉 This makes agents more powerful for orchestration

📌 Docs:  
https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/customization-cheat-sheet

---

## 5. Skills Are NOT Guaranteed to Load

- Skills load only if Copilot thinks they are relevant
- Same prompt → different behavior sometimes

Agents:

- Always active when invoked
- More predictable

📌 Docs:  
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/add-skills

---

## 6. Custom Instructions Add Another Layer

- Always loaded at session start
- Skills = conditional
- Agents = explicit

👉 This creates layered behavior differences

📌 Docs:  
https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features

---

# 🧠 Mental Model

| Component              | Role |
|----------------------|------|
| Custom Instructions   | House rules |
| Skill                | Optional tool card |
| Agent               | Specialist you assign |
| Subagent            | Isolated specialist |

---

# 🔄 Behavior Comparison

### Calling a Skill Directly
- Conditional loading
- Less structured
- Context-dependent
- Can feel inconsistent

### Calling Agent with Skills
- Agent defines behavior first
- Skills enhance capability
- More stable + predictable
- Better for workflows

---

# 🏗️ Recommended Design (Enterprise)

For Spring Boot / Java Architect setup:

## Agent (Orchestrator)
- `engineering-workflow-agent.md`

## Skills (Reusable)
- `security-review-skill.md`
- `runtime-exception-skill.md`
- `spring-jdbc-best-practices-skill.md`
- `redis-kafka-integration-skill.md`

## Global Instructions
- `copilot-instructions.md`

---

# ✅ Rule of Thumb

### Use Skill When:
- Narrow capability
- Reusable across projects
- OK if conditionally loaded

### Use Agent When:
- You need deterministic behavior
- You want structured output
- You need orchestration

### Use Agent + Skills When:
- You want stability + modularity
- You are building enterprise workflows

---

# 🔥 Key Insight

> Skill = "Use this if helpful"  
> Agent = "You are this role"

That single difference explains most behavior gaps.