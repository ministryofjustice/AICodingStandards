# MoJ AI Coding Environment (AICE) – Agent instructions

When acting in this repository, follow Ministry of Justice technical guidance and coding standards summarised below.

## Global rules

### PII and GitHub – Never upload PII

**Critical**: Never upload Personally Identifiable Information (PII) to any MoJ GitHub repository.
PII includes birthdate, race, passport/NI number, or any data that could identify an individual.
Keep secrets separate from source code and never commit them.
Secret scanning is enforced across all repos; if a secret is detected, remediation is mandatory.


### Use the MoJ GitHub organisation for all code

All code produced for MoJ — application code, infrastructure code, and configuration — must be stored in the
ministryofjustice GitHub organisation. Personal accounts, GitLab, Bitbucket, or any other platform are not permitted.
Repos must comply with MoJ GitHub security baselines: branch protection, restricted GITHUB_TOKEN permissions,
and least-privilege workflow permissions by default.


### Follow MoJ OCTO strategic policies and standards

Apply the MoJ Chief Technology Officer's strategic policies and standards published at https://ministryofjustice.github.io/octo-strategic-docs.
These are the authoritative CTO-level policies governing architecture, technology choices, and engineering practice across MoJ.
Consult them when making significant design or technology decisions.


## Principles

### Share the knowledge

If you have unique knowledge, share it. Use GitHub flow: small, short-lived branches.
All non-throwaway code must be reviewed. Package reusable work (e.g. PyPI, rubygems) and share via MoJ Reusables where appropriate.


### Code should be correct, clear, concise – in that order

Correct means provably correct – with tests. All fixes and new features must include tests.
Choose clarity over cleverness; avoid monkey-patching and meta-programming unless justified.
DRY: apply the Rule of Three for duplication. Less code is better, but not at the expense of clarity.


### Optimize for change

Focus on making code easy to change. Don't prematurely optimize – choose clarity over performance unless there is a serious performance issue.


### Something simple which exists is better than a perfect solution which doesn't

Get it done, get it in front of users, learn early. Don't over-engineer. Follow Least Surprise.
Don't roll your own crypto. Handle exceptions at the app level. Use process concurrency over threading unless there is good reason.


### Everything fails, all of the time

Code defensively when calling other services. Every HTTP call can error or hang – handle failures and fail fast.
Don't let long-running external calls harm user experience.


### Other developers are users too

If you have to explain how your code works, it's not clear enough. Comments explain *why*, not *how*.
Commit messages: follow GDS guidance (e.g. type(scope): description). APIs need designing for usability. Don't pollute the global namespace.


### Think smaller

Single Responsibility Principle. Keep views, controllers, models simple; keep methods short.
Many small simple things are better than one big complex thing. Consider Null Object, Facade, Form Objects, Sandi Metz's rules.


### Names have power – use them wisely

Don't be cute or jokey. Names convey meaning; well-named functions and variables can remove the need for comments.
Avoid meaningless names (obj, result, foo). Use single-letter variables only for well-known maths (e.g. e = mc²) or when meaning is clear.
Names should be self-descriptive. Avoid puns, uncommon acronyms, version numbers, or brand names in ways that obscure purpose.


### Composition over inheritance

Prefer 'has-a' over 'is-a' (e.g. Car has-a Motor, not Car is-a MotorVehicle). Inheritance trees often create tech debt.


## Coding standards

### General coding standards

- Comment only where necessary; prefer self-explanatory code.
- camelCase for variables, PascalCase for classes.
- Avoid hard-coded values; use configuration or constants.
- Max line length 120 characters.
- Meaningful names for variables, classes, methods.
- Follow language-specific style guides (e.g. PEP 8 for Python, Google Java style for Java).


### Version control and branching

Use GitHub for all projects (in the ministryofjustice org). Branching: feature/* for features, develop for integration, main for production-ready code.
Commit messages: include ticket/issue reference; format type(scope): description (e.g. feat(auth): add JWT authentication); imperative mood.
Mandatory code review before merging to main (readability, test coverage, security).
Apply branch protection and least-privilege GITHUB_TOKEN permissions to all repositories.


### Design standards and API-first

Apply SOLID: single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion.
Use design patterns where appropriate (e.g. Factory, Observer). Document architecture with UML for complex systems.
**API-First by default**: all new systems must expose their key capabilities via well-documented APIs.
APIs must follow MoJ RESTful design standards: resource-oriented, consistent naming, clear versioning (e.g. /v1/users),
OpenAPI/Swagger documentation, and published to the central MoJ API catalogue.
APIs must use MoJ Zero Trust security controls (OIDC, OAuth2, mTLS where required).
Breaking changes require a new major version; deprecation timelines must be communicated to consumers.
APIs must define and monitor SLOs for latency, throughput, and uptime.


### Integration and data architecture

All real-time and near-real-time integrations must use the MoJ Integration Hub. Point-to-point connections
are prohibited without a formal TDA waiver.
Use event-driven (publish/subscribe) as the default pattern for data movement.
Use canonical data objects for cross-domain data sharing; do not define bespoke formats for shared data.
Data required for analytics or reporting must be managed via the federated data mesh (Justice Data Platform).
Every dataset must have a clearly defined Data Owner and Data Steward.


### Service level classification

All new systems must be classified against the MoJ 5-tier criticality framework during design.
Architecture decisions (HA, DR, backup frequency, geo-redundancy) must be driven by the chosen level:
  Level 1 (Mission Critical): RTO 0–15 min, RPO ~0 — multi-region active-active, automated failover.
  Level 2 (Business Critical): RTO 4–8 hr, RPO <1 hr — warm standby, daily/sub-hourly backups.
  Level 3 (Operational): RTO <24 hr, RPO 4–24 hr — cold/warm DR, daily backups.
  Level 4 (Administrative): RTO 1–3 days, RPO 1–2 days — standard backup and restore.
  Level 5 (Non-Critical): RTO days–weeks — fix-on-failure, minimal DR.
Re-evaluate classification at each major change or upgrade.


### Use MoJ foundational platforms by default

Deliver services using MoJ foundational platforms where they exist and are suitable: Cloud Platform,
Modernisation Platform, and centrally managed identity, CI/CD, and observability services.
Do not introduce parallel hosting stacks or duplicate shared services without formal TDA architectural approval.
Any deviation must have written rationale, risk assessment, and a time-bounded remediation plan.


### Technology choices – MoJ Technology Radar

The MoJ Technology Radar is a governance constraint, not a suggestion.
Before introducing any technology, library, framework, or tool, check https://tech-radar.justice.gov.uk/.
Technologies marked as not recommended, replacement-only, or candidates for retirement must not be introduced into new services.
Prefer technologies in the **Adopt** ring. Raise exceptions early through the Technical Design Authority (TDA) — do not diverge by default.


### Testing standards

All code must pass automated tests in CI/CD before deployment. Test failures must block deployment.
Minimum 70% unit test coverage for new code; higher coverage required for critical paths.
Integration tests required for all major workflows. Tests and assertions must be meaningful.
Provide visibility of test results, coverage metrics, and pipeline status.


### Security standards

Follow UK government Secure by Design principles throughout the service lifecycle — not only at onboarding.
Enable MoJ-mandated automated security scanning: code scanning (SAST), secret scanning, and dependency review in all CI/CD pipelines.
Keep dependencies updated. Secure auth (OAuth 2.0/OIDC, JWT). Encrypt sensitive data at rest (AES-256) and in transit (TLS).
Parameterised queries to prevent SQL injection. Validate all relevant inputs (server and client).
Implement audit logging to support forensic investigation. Systems must support legally admissible investigation activity.


### Deployment and CI/CD

Enforce quality gates at each pipeline stage:
  Build: code compilation, linting, and static analysis.
  Test: automated functional and integration tests; minimum 70% coverage for new code.
  Security: SAST, dependency scanning, and secret detection. Failures block deployment.
  Deployment: automated deployment to non-production then production, with approval controls.
Deploy to staging before production. Keep environment-specific config secure (e.g. Azure Key Vault).
Use GitHub Actions or Azure DevOps. Third-party GitHub Actions must be explicitly approved and version-pinned.


## Frontend and accessibility

### HTML and CSS standards

Use semantic HTML and accessibility attributes (ARIA). Minimise !important; maintain specificity hierarchy.
Avoid inline styles; use external stylesheets or CSS-in-JS. Keep CSS modular (e.g. BEM, CSS Modules, Tailwind).


### JavaScript/TypeScript frontend

Enforce strict typing with TypeScript. Use ES6+. Implement error handling; avoid silent failures.
Avoid global variables; use modules or closures. Use ESLint. Prefer React, Angular, or Vue as approved; state management Redux or Zustand.


### Accessibility (WCAG AA)

Meet WCAG 2.2 Level AA as the internal standard (WCAG 2.1 Level AA is the external supplier minimum).
Use GOV.UK Design System components. Alt text for images, ARIA for dynamic elements, keyboard navigation, focus management.
Test with screen readers and automated tools (Axe, Pa11y, WAVE) AND with real users using assistive technologies.
Support browser zoom to 400%; logical headings; meaningful link text; descriptive page titles; colour contrast.
Design accessibility in from the start: include accessibility requirements in user stories and acceptance criteria,
test each sprint, include accessibility checks in code review, and remediate defects with same priority as security bugs.


### Government Service Manual

Follow the Government Service Design Manual. Services are assessed against it before going live.
Use verified browsers list; responsive design; progressive enhancement.


## Naming and licensing

### Naming things

Names must be self-descriptive. Avoid puns, uncommon acronyms, version numbers, or brand names that obscure purpose.
Use the same name consistently (e.g. GitHub repo name matches hostname). Prefer: Peoplefinder, Send Money to a Prisoner, Help with Fees.
Avoid: ambiguous names, internal acronyms (e.g. CCCD, PVB2, DOMIS).


### Licensing software or code

MoJ uses the MIT License. Each repo must include LICENCE or LICENCE.md with full licence text.
Copyright: "Copyright (c) YYYY Crown Copyright (Ministry of Justice)". Use UK spelling "Licence" where preferred.
When reusing others' work, provide proper attribution in the licence file.


## AI governance

### Use only approved MoJ AI coding tools

The approved MoJ AI coding assistant portfolio is: GitHub Copilot, OpenAI Codex, Claude Code (via Azure Foundry),
Cursor, and AWS Kiro. Use only tools from this approved list.
Review all AI-generated outputs for accuracy before use. Engineers remain accountable for code quality and safety.


### LLM access – Justice AI Gateway and Azure AI Foundry only

All LLM usage within MoJ must go through Justice AI Gateway (default, AWS-first) or Azure AI Foundry.
Direct integration with external LLM APIs is not permitted. Personal or team-managed API keys for LLM services are not permitted.
MoJ data must not be sent to AI services outside these approved platforms.
New models or platforms require TDA approval before use.


### Use only permitted LLM models

Before using any LLM model, check the MoJ Permitted LLM Models registry at
https://ministryofjustice.github.io/octo-strategic-docs/draft/permitted-llm-ai-models-policy.html.
The registry has three status categories:
  **Approved** – available for general use without further approval.
  **Exception** – requires explicit written approval from the CTO or TDA before use. Liaise with OCTO/Justice.AI first.
  **Not Approved** – must not be used for any MoJ workload without exceptional CTO/TDA approval.
  **Unknown** – must not be used without prior TDA assessment and approval.
Models not listed in the registry must not be used without prior TDA assessment.

Approved models include: OpenAI GPT-4o, GPT-4.1, GPT-5.1/5.3/5.4; Anthropic Claude 3.5/3.7 Sonnet, Claude 3 Opus, Claude 3.5 Haiku;
Meta Llama 2/3/4; Mistral Large 3, Ministral 3, Mistral Document AI; Cohere Command A, Embed 3.0, Rerank 4.0;
Microsoft Phi-3, Phi-3.5; Amazon Titan Embeddings 2.0; Google Gemini 2.0, Gemini 2.5.

Exception models (explicit CTO/TDA approval required): OpenAI GPT-5.5, o1, o3, o3-mini, o3-pro, GPT-OSS 1.0; xAI Grok 4.x; OpenAI Sora 1.0.

Not Approved (must not use without exceptional approval): all DeepSeek variants (R1, 3.x, 4.x, Coder);
all Qwen/Alibaba models (Qwen 3, Qwen 3 Coder); all Kimi/Moonshot models.

Unknown status (TDA assessment needed): Google Gemma 2, Gemma 3.

Newer versions/patches of existing Approved model families may be used pending formal registry updates,
but teams must notify OCTO so the registry can be kept current. This does not apply to entirely new models or families.

Note: AI coding tools (GitHub Copilot, Cursor, etc.) are out of scope of this policy — they are governed
through their own TDA product assessment, not the LLM model registry.

All models must run on segregated MoJ infrastructure. Vendors must guarantee prompts are not used for model training.
AI-generated content must not reproduce third-party IP; where platforms offer a filter to block this (e.g. Copilot
duplication detection), it must be enabled.


### Build AI-enabled services safely

Send only the minimum data required to any model. Follow MoJ data classification; avoid personal or sensitive data unless explicitly approved.
Treat all LLM-generated outputs as untrusted: validate them, apply quality assurance, and do not base critical decisions solely on model outputs.
Protect against prompt injection and similar attacks. Validate inputs and outputs. Maintain audit logging.
Enable duplication detection filters where available (e.g. Copilot's duplication detection filter must be enabled).
AI-generated content must not reproduce third-party IP without appropriate licensing rights.
Where AI affects service outcomes, be transparent: clearly identify AI use to users, explain limitations, and provide escalation routes.


### AI governance and human accountability

No ingestion of personal data or sensitive security data by AI unless TDA-approved.
Document AI use within services; maintain transparency and auditability.
Delivery teams remain accountable for the systems they build — approved platforms do not transfer responsibility
for security, data protection, service quality, or user outcomes.


---
*Canonical source: [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/).*
