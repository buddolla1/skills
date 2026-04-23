# Skill: spring-structure-detector

## Purpose
Identify Spring layers, package boundaries, configuration style, and architecture signals.

## When To Use
Use this skill when reviewing controllers, services, repositories, configs, or bootstrap code.

## Instructions
- Detect controllers, services, repositories, configs, exception handlers, interceptors, filters, schedulers, listeners, and integrations.
- Identify whether the code is layered, modular monolith, microservice, or hybrid.
- Flag violations such as direct controller-to-repository calls or config sprawl.
- Reuse the structural rules from [architecture-and-coding.md](../../../../instructions/topics/architecture-and-coding.md).

## Output
- Architecture style
- Layering and boundary issues
- Structure risks
