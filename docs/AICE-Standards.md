# MoJ AI Coding Environment (AICE) Standards

Human-readable reference for Ministry of Justice coding standards, principles, and guidelines used by AI coding tools (Cursor, GitHub Copilot, Claude Code, AWS Kiro, etc.).

*Generated from `source/standards.yaml` (version 1.0.0).*

## Canonical sources

| Document | Link |
|----------|------|
| MoJ Technical Guidance | [link](https://technical-guidance.service.justice.gov.uk/) |
| Justice Digital software engineering standards | [justice-digital-software-engineering-standards.html](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-software-engineering-standards.html) |
| Justice Digital front end engineering standards | [justice-digital-front-end-engineering-standards.html](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-front-end-engineering-standards.html) |
| Development Principles | [development-principles.html](https://technical-guidance.service.justice.gov.uk/documentation/principles/development-principles.html) |
| Frontend Development Principles | [frontend-development-principles.html](https://technical-guidance.service.justice.gov.uk/documentation/principles/frontend-development-principles.html) |
| Naming things | [naming-things.html](https://technical-guidance.service.justice.gov.uk/documentation/standards/naming-things.html) |
| Licensing software or code | [licencing-software-or-code.html](https://technical-guidance.service.justice.gov.uk/documentation/standards/licencing-software-or-code.html) |
| MOJ Engineering AI Governance Framework | [ai-governance-framework.html](https://technical-guidance.service.justice.gov.uk/documentation/governance/ai-governance-framework.html) |
| ministryofjustice GitHub | [ministryofjustice](https://github.com/ministryofjustice) |
| Template repository | [template-repository](https://github.com/ministryofjustice/template-repository) |
| MoJ OCTO Strategic Policies and Standards | [octo-strategic-docs](https://ministryofjustice.github.io/octo-strategic-docs) |
| MoJ Technology Radar | [link](https://tech-radar.justice.gov.uk/) |
| MoJ AI Coding Assistant Strategy | [ai-coding-assistant-strategy.html](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-coding-assistant-strategy.html) |
| MoJ AI Platform Access Policy | [ai-platform-access-policy.html](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-platform-access-policy.html) |
| MoJ Permitted LLM AI Models Policy | [permitted-llm-ai-models-policy.html](https://ministryofjustice.github.io/octo-strategic-docs/draft/permitted-llm-ai-models-policy.html) |
| MoJ Integration and API Strategy | [integration-api-strategy.html](https://ministryofjustice.github.io/octo-strategic-docs/published/integration-api-strategy.html) |
| MoJ Service Level Framework | [service-levels.html](https://ministryofjustice.github.io/octo-strategic-docs/published/service-levels.html) |
| MoJ External Supplier Requirements | [external-supplier-requirements.html](https://ministryofjustice.github.io/octo-strategic-docs/published/external-supplier-requirements.html) |

---

## Summary of standards and principles

### Critical (PII and security)
- **Never upload PII** to MoJ GitHub repositories. Keep secrets out of source code.
- Follow MoJ OCTO strategic policies: https://ministryofjustice.github.io/octo-strategic-docs
- [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/)

### Development principles
- Share knowledge; use GitHub flow; all non-throwaway code reviewed.
- Code: correct (with tests), clear, concise. Optimize for change.
- Something simple that exists beats a perfect solution that doesn't.
- Everything fails: code defensively; fail fast; don't block UX on long external calls.
- Other developers are users: clear code, good commit messages, usable APIs.
- Think smaller: Single Responsibility; small methods; composition over inheritance.
- Names: self-descriptive; avoid puns, obscure acronyms, version numbers in names.
- [Development Principles](https://technical-guidance.service.justice.gov.uk/documentation/principles/development-principles.html)

### Coding standards
- General: camelCase/PascalCase, max line 120, config not hard-coding, language style guides.
- Version control: GitHub; feature/ branches; commits `type(scope): description`; mandatory review.
- Design: SOLID; versioned APIs; OpenAPI/Swagger; UML for complex systems.
- Technology choices: check the MoJ Technology Radar (https://tech-radar.justice.gov.uk/) before introducing new tools.
- Testing: integration tests for major workflows; automated frameworks; meaningful coverage.
- Security: vulnerability scanning; parameterised queries; input validation; encrypt sensitive data.
- CI/CD: tests on every commit; staging before production; secure config (e.g. Key Vault).
- [Justice Digital software engineering standards](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-software-engineering-standards.html)

### Frontend and accessibility
- Semantic HTML; ARIA; GOV.UK Design System; WCAG 2.2 AA; keyboard and screen reader testing.
- Responsive design; progressive enhancement; no premature optimisation.
- [Justice Digital front end engineering standards](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-front-end-engineering-standards.html)
- [Frontend Development Principles](https://technical-guidance.service.justice.gov.uk/documentation/principles/frontend-development-principles.html)

### Naming
- Self-descriptive names; consistent (e.g. repo name <-> hostname); avoid ambiguous or internal-only acronyms.
- [Naming things](https://technical-guidance.service.justice.gov.uk/documentation/standards/naming-things.html)

### Licensing
- MIT License; LICENCE or LICENCE.md in each repo; Crown Copyright (Ministry of Justice); proper attribution for reused work.
- [Licensing software or code](https://technical-guidance.service.justice.gov.uk/documentation/standards/licencing-software-or-code.html)

### AI governance
- Use only MoJ-approved AI tools; no sensitive/PII in AI unless TDA-approved; review all AI output; human in the loop.
- [MOJ Engineering AI Governance Framework](https://technical-guidance.service.justice.gov.uk/documentation/governance/ai-governance-framework.html)

---

## How AICE artifacts are built

Run from the repo root:

```bash
pip install pyyaml
python scripts/build_aice.py
```

This generates all artifacts into `dist/`:
- `dist/.cursor/rules/*.mdc`              - Cursor
- `dist/.github/copilot-instructions.md`  - GitHub Copilot / Codex
- `dist/AGENTS.md`                        - OpenAI Codex / Jules / OpenCode
- `dist/CLAUDE.md`                        - Claude Code
- `dist/.kiro/steering/*.md`              - AWS Kiro

CI/CD can run the same script (see `.github/workflows/build-aice.yml`).
