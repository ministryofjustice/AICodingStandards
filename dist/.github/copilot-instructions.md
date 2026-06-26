# MoJ Repository – AI Coding Standards

This repository follows **Ministry of Justice (MoJ) Technical Guidance** and Justice Digital standards. Apply these when generating or modifying code.

## Critical
- **Never** upload PII (personally identifiable information) or secrets to this repo.
- Use GitHub for version control; feature branches; commits: `type(scope): description`; mandatory review before merge.
- **Use the MoJ GitHub organisation for all code:** All code produced for MoJ — application code, infrastructure code, and configuration — must be stored in the
- **Follow MoJ OCTO strategic policies and standards:** Apply the MoJ Chief Technology Officer's strategic policies and standards published at https://ministryofjustice.github.io/octo-strategic-docs.

## Code quality
- Correct, clear, concise (in that order). Tests required for fixes and new features.
- Meaningful names; avoid globals; comment only when necessary (explain why, not how).
- Prefer composition over inheritance; small, single-responsibility units.
- Follow language style guides (e.g. PEP 8 for Python). Max line length 120.

## Design & APIs
- SOLID principles; versioned APIs (e.g. /v1/...); OpenAPI/Swagger; RESTful.

## Technology choices – MoJ Technology Radar
- The MoJ Technology Radar is a governance constraint, not a suggestion.
- Before introducing any technology, library, framework, or tool, check https://tech-radar.justice.gov.uk/.
- Technologies marked as not recommended, replacement-only, or candidates for retirement must not be introduced into new services.
- Prefer technologies in the **Adopt** ring. Raise exceptions early through the Technical Design Authority (TDA) — do not diverge by default.

## Security
- Parameterised queries; validate inputs; secure auth (OAuth 2.0/JWT); encrypt sensitive data; keep dependencies updated.

## Frontend (when touching HTML/CSS/JS/TS)
- Semantic HTML; accessibility (WCAG 2.2 AA); GOV.UK Design System where applicable; no inline styles; BEM/CSS Modules.

## Licensing
- MoJ uses MIT; Crown Copyright (Ministry of Justice). Include LICENCE in repo.

## AI use
- Use only approved MoJ AI tools; review all AI-generated output; no sensitive data into AI unless approved.

Source: [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/).
