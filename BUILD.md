# Build AICE Artifacts

This repository is a generator pipeline.

The single source of truth is `source/standards.yaml`. Build outputs are generated into `dist/` and `docs/AICE-Standards.md`.

Important: do not edit files inside `dist/` directly. They are regenerated on every build.

## Prerequisites

- Python 3.11
- `pip`

## Local build

Run from the repository root:

```bash
pip install -r requirements.txt
python scripts/build_aice.py
```

## Verify generated outputs

```bash
find dist/ -type f | sort
```

Expected outputs include:

- `dist/.github/copilot-instructions.md`
- `dist/AGENTS.md`
- `dist/CLAUDE.md`
- `dist/.cursor/rules/*.mdc`
- `dist/.kiro/steering/*.md`
- `docs/AICE-Standards.md`

## CI/CD build

GitHub Actions workflow:

- `.github/workflows/build-aice.yml`

Trigger conditions:

- Push to `main` that changes `source/**` or `scripts/**`
- Manual workflow run

CI artifact:

- `aice-artifacts`

## Build when contributing

If you submit changes, build locally before opening a PR so generated files stay in sync.

Typical flow:

1. Edit `source/standards.yaml` (and `scripts/build_aice.py` only if generator logic changes).
2. Run local build.
3. Verify generated outputs.
4. Commit source plus regenerated outputs together.
