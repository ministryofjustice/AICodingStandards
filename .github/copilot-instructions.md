# MoJ AICodingStandards – Contributor Instructions

This repo is a **build pipeline**, not a coding environment. It reads `source/standards.yaml` and generates AI instruction files for all MoJ-approved AICE tools, outputting them to `dist/` for repo owners to copy.

## Build

```bash
pip install -r requirements.txt
python scripts/build_aice.py
```

Verify with:

```bash
find dist/ -type f | sort
```

## Architecture

```
source/standards.yaml   ← single source of truth; edit here
        ↓
scripts/build_aice.py   ← reads YAML, renders each tool's format
        ↓
dist/
  .github/copilot-instructions.md   (GitHub Copilot / Codex)
  .cursor/rules/*.mdc               (Cursor)
  AGENTS.md                         (OpenAI Codex / Jules / OpenCode)
  CLAUDE.md                         (Claude Code)
  .kiro/steering/*.md               (AWS Kiro)

docs/AICE-Standards.md             ← human-readable reference (not for dist)
```

CI (`.github/workflows/build-aice.yml`) rebuilds `dist/` automatically on push to `main` when `source/**` or `scripts/**` change.

## Key conventions

- **Never edit files in `dist/` directly.** They are fully regenerated on every build (`dist/` is deleted and recreated). All changes must go into `source/standards.yaml`.
- **`standards.yaml` structure:** top-level keys are `global_rules`, `principles`, `coding_standards`, `frontend_standards`, `naming_standards`, `licensing_standards`, `ai_governance`, `python_standards`, `ruby_standards`. Each entry needs `id`, `title`, `source_url`, and `content`. Optional `globs` field for file-type scoping.
- **Adding a new AICE tool:** add a `write_<toolname>()` function in `build_aice.py` that writes to `dist/`, call it from `main()`, and document the output path in the README.
- Commit format: `type(scope): description` — e.g. `feat(yaml): add java standards`, `fix(kiro): correct fileMatchPattern`.
- Python target: 3.11. Follow PEP 8; specify exception types in `try/except`.

## Canonical sources

- [MoJ OCTO Strategic Policies](https://ministryofjustice.github.io/octo-strategic-docs) — CTO-level, authoritative
- [MoJ Technology Radar](https://tech-radar.justice.gov.uk/) — approved/prohibited technology choices
- [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/)
