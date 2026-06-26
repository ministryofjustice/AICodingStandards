# MoJ AI Coding Environment (AICE) Standards

Ministry of Justice (UK) **AI Coding Environment standards** for use with GitHub Copilot, Cursor, Claude Code, AWS Kiro, OpenAI Codex, and other approved MoJ AI coding tools. This repo is the single source of truth and build pipeline for MoJ coding standards consumed by AI assistants.

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

## For repo owners: adding MoJ AICE standards to your repo

Copy the relevant files from `dist/` into your repository. You only need the files for the tools your team uses.

### Copy all tools at once

```bash
# From the root of your target repo
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

Or clone this repo and copy `dist/` manually:

```bash
git clone https://github.com/ministryofjustice/AICodingStandards.git
cp -r AICodingStandards/dist/.github   your-repo/
cp -r AICodingStandards/dist/.cursor   your-repo/
cp -r AICodingStandards/dist/.kiro     your-repo/
cp    AICodingStandards/dist/AGENTS.md your-repo/
cp    AICodingStandards/dist/CLAUDE.md your-repo/
```

### What each file does

| File | Tool | How it is picked up |
|------|------|---------------------|
| `.github/copilot-instructions.md` | GitHub Copilot, Codex | Automatically by GitHub Copilot for any repo it's enabled on |
| `CLAUDE.md` | Claude Code | Automatically when Claude Code opens the repo |
| `AGENTS.md` | OpenAI Codex, Jules, OpenCode | Automatically from the repo root |
| `.cursor/rules/*.mdc` | Cursor | Automatically applied (global rules always; language rules by file match) |
| `.kiro/steering/*.md` | AWS Kiro | Applied per the `inclusion` frontmatter (`always` or `fileMatch`) |

### Merging with existing instruction files

If your repo already has any of these files, merge rather than overwrite. Keep your repo-specific context (architecture, build commands, etc.) alongside the MoJ standards blocks so they can be updated independently.

### Keeping up to date

Re-run the copy commands above whenever standards change. CI rebuilds `dist/` automatically when `source/standards.yaml` is updated.

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

---

## Rebuilding AICE artifacts

All generated artifacts are rebuilt from `source/standards.yaml`. **Do not edit generated files directly.**

### Local build

```bash
pip install -r requirements.txt
python scripts/build_aice.py
```

Generated/updated:

- `dist/`  ← copy this to your repos
- `docs/AICE-Standards.md`

### CI/CD (GitHub Actions)

- Workflow: **`.github/workflows/build-aice.yml`**
- Triggers: push to `main` that touches `source/**` or `scripts/**`, or manual **Run workflow**.
- Uploads the generated `dist/` as the **aice-artifacts** artifact.

## Updating standards

1. Edit **`source/standards.yaml`**.
2. Run `python scripts/build_aice.py` locally, or push and let CI rebuild.
3. Commit `source/standards.yaml`, the updated `dist/` contents, and `docs/AICE-Standards.md`.

## Licence

Crown Copyright (Ministry of Justice). See [LICENCE](LICENCE) in this repo (or apply MoJ's standard MIT licence as per [MoJ licensing guidance](https://technical-guidance.service.justice.gov.uk/documentation/standards/licencing-software-or-code.html)).
