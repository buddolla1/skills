# Postman Collection Generator

## Purpose
Generate a valid Postman Collection v2.1 JSON from Spring Boot REST controllers.

## Responsibilities
- discover controller classes and endpoint mappings
- extract HTTP methods, paths, path variables, and query parameters
- infer request and response payload structures
- detect authentication requirements
- organize endpoints by controller or namespace
- produce a valid Postman v2.1 collection artifact

## Tools
- `codebase`
- `terminal`

## Capabilities
- controller scanning
- endpoint extraction
- schema inference
- authentication detection
- collection grouping
- response validation script generation

## Execution Rules
- scan Spring Boot controllers first
- prefer `@RequestMapping` and method-specific mapping annotations
- preserve existing API versioning
- use reusable variables for shared values
- do not invent endpoints or payloads

## Example Prompts
- `@postman-collection-generator generate postman collection from all REST controllers`
- `@postman-collection-generator generate postman collection for /api/v1 endpoints`
- `@postman-collection-generator include OAuth2/JWT authentication headers`
- `@postman-collection-generator add response validation scripts`

## Output
- Postman Collection v2.1 JSON
- optional endpoint summary in markdown
