# MoJ AI Coding Environment (AICE) Standards

Ministry of Justice (UK) **AI Coding Environment standards** for use with GitHub Copilot, Cursor, Claude Code, AWS Kiro, OpenAI Codex, and other approved MoJ AI coding tools. This repo is the single source of truth and build pipeline for MoJ coding standards consumed by AI assistants.

## Why this matters

This repository turns MoJ AI policy into practical, reusable instruction files that teams can apply consistently across repositories and tools.

Without this, standards are likely to drift between teams and products. With this repo, policy requirements are encoded once in `source/standards.yaml` and then generated into each tool's expected format in `dist/`.

The policy context is:

- **Approved AI coding tool portfolio**: the MoJ [AI Coding Assistant Strategy](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-coding-assistant-strategy.html) defines which coding assistants are approved for use.
- **Approved AI platform access model**: the [AI Platform Access Policy](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-platform-access-policy.html) defines where LLM access must happen (Justice AI Gateway or Azure AI Foundry), and prohibits unmanaged direct API usage.
- **Permitted LLM model controls**: the [Permitted LLM AI Models Policy](https://ministryofjustice.github.io/octo-strategic-docs/draft/permitted-llm-ai-models-policy.html) defines model approval states and usage restrictions.
- **Safe use and accountability expectations**: the [AI Platform Access Policy](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-platform-access-policy.html) and [MOJ Engineering AI Governance Framework](https://technical-guidance.service.justice.gov.uk/documentation/governance/ai-governance-framework.html) set requirements for data handling, validation of AI outputs, transparency, and delivery team accountability.

In short: this repo helps teams apply policy-aligned defaults quickly, while still keeping accountability with engineers and service teams.

## What's in this repo

| Item | Purpose |
|------|---------|
| **`source/standards.yaml`** | **Edit here.** Single source of truth for all standards. All other files below are generated from this. |
| **`scripts/build_aice.py`** | Build script: reads `source/standards.yaml` and regenerates everything in `dist/` and `docs/AICE-Standards.md`. |
| **`dist/`** | **Copy from here.** All generated artifacts, ready for repo owners to copy into their own repos. |
| **`.github/workflows/build-aice.yml`** | CI/CD: runs the build on push to `source/**` or `scripts/**`, or manually; uploads artifacts. |
| **`docs/AICE-Standards.md`** | Human-readable reference with links to canonical MoJ sources. |

The root `.github/copilot-instructions.md` is a handcrafted contributor guide for working **in this repo** — it is not generated and not intended for copying.

## Approved AICE tools

Per the [MoJ AI Coding Assistant Strategy](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-coding-assistant-strategy.html), the approved portfolio is:

| Tool | Instruction file generated |
|------|---------------------------|
| **GitHub Copilot** | `dist/.github/copilot-instructions.md` |
| **Codex** (via existing enterprise agreement) | `dist/AGENTS.md` |
| **Claude Code** (via Azure Foundry) | `dist/CLAUDE.md` |
| **Cursor** | `dist/.cursor/rules/*.mdc` |
| **AWS Kiro** | `dist/.kiro/steering/*.md` |

---

## How to use this as a developer or repo owner

Use this repository as a source of ready-to-copy AI instruction files for MoJ-approved tools, whether you are an individual developer setting up a codebase or a repo owner maintaining standards across a team.

### Step 1: Pick the tools you or your team uses

| File in this repo (`dist/`) | Tool | Put this file in your repo |
|------|------|---------------------|
| `.github/copilot-instructions.md` | GitHub Copilot, Codex | `.github/copilot-instructions.md` |
| `CLAUDE.md` | Claude Code | `CLAUDE.md` |
| `AGENTS.md` | OpenAI Codex, Jules, OpenCode | `AGENTS.md` |
| `.cursor/rules/*.mdc` | Cursor | `.cursor/rules/*.mdc` |
| `.kiro/steering/*.md` | AWS Kiro | `.kiro/steering/*.md` |

### Step 2: Copy generated files from `dist/`

Run from the root of the repository you are working in:

```bash
AICE_REPO=https://raw.githubusercontent.com/ministryofjustice/AICodingStandards/main/dist

# GitHub Copilot / Codex
mkdir -p .github
curl -fsSL $AICE_REPO/.github/copilot-instructions.md -o .github/copilot-instructions.md

# Claude Code
curl -fsSL $AICE_REPO/CLAUDE.md -o CLAUDE.md

# OpenAI Codex / Jules / OpenCode
curl -fsSL $AICE_REPO/AGENTS.md -o AGENTS.md

# Cursor
mkdir -p .cursor/rules
for f in moj-global moj-coding-standards moj-frontend moj-python moj-ruby; do
  curl -fsSL $AICE_REPO/.cursor/rules/$f.mdc -o .cursor/rules/$f.mdc
done

# AWS Kiro
mkdir -p .kiro/steering
for f in moj-global moj-coding-standards moj-frontend moj-python moj-ruby; do
  curl -fsSL $AICE_REPO/.kiro/steering/$f.md -o .kiro/steering/$f.md
done
```

Alternative: clone this repo and copy from `dist/` manually.

```bash
git clone https://github.com/ministryofjustice/AICodingStandards.git
cp -r AICodingStandards/dist/.github   your-repo/
cp -r AICodingStandards/dist/.cursor   your-repo/
cp -r AICodingStandards/dist/.kiro     your-repo/
cp    AICodingStandards/dist/AGENTS.md your-repo/
cp    AICodingStandards/dist/CLAUDE.md your-repo/
```

### Step 3: Merge if files already exist

If the repository already has instruction files, merge content instead of overwriting. Keep existing service context (architecture, local build commands, deployment notes) with the imported MoJ standards.

### Step 4: Keep your repository up to date

Re-copy files from `dist/` when this repository updates. Generated files in `dist/` are the supported files for teams and developers to consume.

## How to build the content for others to consume

Build and verification instructions are in [BUILD.md](BUILD.md).

## How to submit changes to this repository

### What to change

1. Update standards in `source/standards.yaml`.
2. Only edit `scripts/build_aice.py` when changing generation logic or adding a new output format.
3. Do not hand-edit files under `dist/`.

### Change workflow

1. Create a branch from `main`.
2. Make your change in `source/standards.yaml` (and script changes if required).
3. Follow [BUILD.md](BUILD.md) to run the local build and verify generated files.
4. Commit source and regenerated outputs together:
   - `source/standards.yaml`
   - updated `dist/` files
   - updated `docs/AICE-Standards.md`
5. Use commit format: `type(scope): description` (example: `feat(yaml): add policy links`).
6. Open a pull request to `main` with a short summary of:
   - what policy or standard changed
   - why it changed
   - which generated outputs were updated

---

## Canonical sources (MoJ)

Standards are derived from:

- [MoJ OCTO Strategic Policies and Standards](https://ministryofjustice.github.io/octo-strategic-docs) ← CTO-level policies, **authoritative**
- [MoJ AI Coding Assistant Strategy](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-coding-assistant-strategy.html)
- [MoJ AI Platform Access Policy](https://ministryofjustice.github.io/octo-strategic-docs/draft/ai-platform-access-policy.html)
- [MoJ Permitted LLM AI Models Policy](https://ministryofjustice.github.io/octo-strategic-docs/draft/permitted-llm-ai-models-policy.html)
- [MoJ Integration and API Strategy](https://ministryofjustice.github.io/octo-strategic-docs/published/integration-api-strategy.html)
- [MoJ Service Level Framework](https://ministryofjustice.github.io/octo-strategic-docs/published/service-levels.html)
- [MoJ External Supplier Requirements](https://ministryofjustice.github.io/octo-strategic-docs/published/external-supplier-requirements.html)
- [MoJ Technology Radar](https://tech-radar.justice.gov.uk/) ← approved/prohibited technology choices
- [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/)
- [Justice Digital software engineering standards](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-software-engineering-standards.html)
- [Justice Digital front end engineering standards](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-front-end-engineering-standards.html)
- [Development Principles](https://technical-guidance.service.justice.gov.uk/documentation/principles/development-principles.html)
- [Frontend Development Principles](https://technical-guidance.service.justice.gov.uk/documentation/principles/frontend-development-principles.html)
- [Naming things](https://technical-guidance.service.justice.gov.uk/documentation/standards/naming-things.html)
- [Licensing software or code](https://technical-guidance.service.justice.gov.uk/documentation/standards/licencing-software-or-code.html)
- [MOJ Engineering AI Governance Framework](https://technical-guidance.service.justice.gov.uk/documentation/governance/ai-governance-framework.html)
- [ministryofjustice GitHub](https://github.com/ministryofjustice)

For how these and other MoJ repos are used to discover and maintain standards, see [docs/Discovering-MoJ-Standards.md](docs/Discovering-MoJ-Standards.md).

## Licence

Crown Copyright (Ministry of Justice). See [LICENCE](LICENCE) in this repo (or apply MoJ's standard MIT licence as per [MoJ licensing guidance](https://technical-guidance.service.justice.gov.uk/documentation/standards/licencing-software-or-code.html)).
