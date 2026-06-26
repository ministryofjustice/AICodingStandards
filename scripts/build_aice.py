#!/usr/bin/env python3
"""
Build AICE (AI Coding Environment) artifacts from source/standards.yaml.

Writes all generated artifacts directly into dist/, covering all MoJ-approved
AI coding environments:

  dist/.github/copilot-instructions.md  -> GitHub Copilot / Codex
  dist/.cursor/rules/*.mdc              -> Cursor
  dist/AGENTS.md                        -> OpenAI Codex / Jules / OpenCode
  dist/CLAUDE.md                        -> Claude Code
  dist/.kiro/steering/*.md              -> AWS Kiro

Also writes docs/AICE-Standards.md (human-readable reference; stays in this repo).

Run from repo root: python scripts/build_aice.py
Or: pip install pyyaml && python scripts/build_aice.py
"""

import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE = REPO_ROOT / "source" / "standards.yaml"
DOCS_DIR = REPO_ROOT / "docs"
DIST_DIR = REPO_ROOT / "dist"


def load_source():
    with open(SOURCE_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_dirs():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    # dist/ is rebuilt from scratch each run
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    for sub in [
        DIST_DIR / ".github",
        DIST_DIR / ".cursor" / "rules",
        DIST_DIR / ".kiro" / "steering",
    ]:
        sub.mkdir(parents=True, exist_ok=True)


def write_cursor_rules(data):
    """Generate dist/.cursor/rules/*.mdc for Cursor."""
    rules_dir = DIST_DIR / ".cursor" / "rules"

    always_parts = []
    for r in data.get("global_rules", []):
        always_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("principles", []):
        always_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (rules_dir / "moj-global.mdc").write_text(
        "---\ndescription: MoJ global rules and development principles (PII, security, principles)\nalwaysApply: true\n---\n\n"
        "# MoJ Global Standards\n\n" + "\n".join(always_parts),
        encoding="utf-8",
    )

    general_parts = []
    for r in data.get("coding_standards", []):
        general_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("naming_standards", []):
        general_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("licensing_standards", []):
        general_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("ai_governance", []):
        general_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (rules_dir / "moj-coding-standards.mdc").write_text(
        "---\ndescription: MoJ coding, design, testing, security, naming, licensing and AI governance\nalwaysApply: false\n---\n\n"
        "# MoJ Coding and Governance Standards\n\n" + "\n".join(general_parts),
        encoding="utf-8",
    )

    frontend_parts = []
    for r in data.get("frontend_standards", []):
        frontend_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (rules_dir / "moj-frontend.mdc").write_text(
        '---\ndescription: MoJ frontend and accessibility standards\nglobs: ["**/*.tsx", "**/*.jsx", "**/*.vue", "**/*.html", "**/*.css", "**/*.scss"]\nalwaysApply: false\n---\n\n'
        "# MoJ Frontend Standards\n\n" + "\n".join(frontend_parts),
        encoding="utf-8",
    )

    python_parts = []
    for r in data.get("python_standards", []):
        python_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (rules_dir / "moj-python.mdc").write_text(
        '---\ndescription: MoJ Python-specific principles\nglobs: ["**/*.py"]\nalwaysApply: false\n---\n\n'
        "# MoJ Python Standards\n\n" + "\n".join(python_parts),
        encoding="utf-8",
    )

    ruby_parts = []
    for r in data.get("ruby_standards", []):
        ruby_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (rules_dir / "moj-ruby.mdc").write_text(
        '---\ndescription: MoJ Ruby-specific principles\nglobs: ["**/*.rb"]\nalwaysApply: false\n---\n\n'
        "# MoJ Ruby Standards\n\n" + "\n".join(ruby_parts),
        encoding="utf-8",
    )


def write_copilot_instructions(data):
    """Generate dist/.github/copilot-instructions.md for GitHub Copilot / Codex."""
    extra_global = [r for r in data.get("global_rules", []) if r["id"] != "pii-and-security"]
    tech_choices = next(
        (r for r in data.get("coding_standards", []) if r["id"] == "technology-choices"), None
    )

    lines = [
        "# MoJ Repository \u2013 AI Coding Standards",
        "",
        "This repository follows **Ministry of Justice (MoJ) Technical Guidance** and Justice Digital standards. Apply these when generating or modifying code.",
        "",
        "## Critical",
        "- **Never** upload PII (personally identifiable information) or secrets to this repo.",
        "- Use GitHub for version control; feature branches; commits: `type(scope): description`; mandatory review before merge.",
    ]
    for r in extra_global:
        lines.append(f"- **{r['title']}:** {r['content'].strip().splitlines()[0]}")
    lines += [
        "",
        "## Code quality",
        "- Correct, clear, concise (in that order). Tests required for fixes and new features.",
        "- Meaningful names; avoid globals; comment only when necessary (explain why, not how).",
        "- Prefer composition over inheritance; small, single-responsibility units.",
        "- Follow language style guides (e.g. PEP 8 for Python). Max line length 120.",
        "",
        "## Design & APIs",
        "- SOLID principles; versioned APIs (e.g. /v1/...); OpenAPI/Swagger; RESTful.",
    ]
    if tech_choices:
        lines += ["", f"## {tech_choices['title']}"]
        for line in tech_choices["content"].strip().splitlines():
            lines.append(f"- {line}" if not line.startswith("-") else line)
    lines += [
        "",
        "## Security",
        "- Parameterised queries; validate inputs; secure auth (OAuth 2.0/JWT); encrypt sensitive data; keep dependencies updated.",
        "",
        "## Frontend (when touching HTML/CSS/JS/TS)",
        "- Semantic HTML; accessibility (WCAG 2.2 AA); GOV.UK Design System where applicable; no inline styles; BEM/CSS Modules.",
        "",
        "## Licensing",
        "- MoJ uses MIT; Crown Copyright (Ministry of Justice). Include LICENCE in repo.",
        "",
        "## AI use",
        "- Use only approved MoJ AI tools; review all AI-generated output; no sensitive data into AI unless approved.",
        "",
        "Source: [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/).",
        "",
    ]
    (DIST_DIR / ".github" / "copilot-instructions.md").write_text("\n".join(lines), encoding="utf-8")


def _agents_md_content(data):
    """Return the full agent instructions content (shared by AGENTS.md and CLAUDE.md)."""
    sections = [
        "# MoJ AI Coding Environment (AICE) \u2013 Agent instructions",
        "",
        "When acting in this repository, follow Ministry of Justice technical guidance and coding standards summarised below.",
        "",
        "## Global rules",
        "",
    ]
    for r in data.get("global_rules", []):
        sections.append(f"### {r['title']}\n\n{r['content']}\n")
    sections.append("## Principles\n")
    for r in data.get("principles", []):
        sections.append(f"### {r['title']}\n\n{r['content']}\n")
    sections.append("## Coding standards\n")
    for r in data.get("coding_standards", []):
        sections.append(f"### {r['title']}\n\n{r['content']}\n")
    sections.append("## Frontend and accessibility\n")
    for r in data.get("frontend_standards", []):
        sections.append(f"### {r['title']}\n\n{r['content']}\n")
    sections.append("## Naming and licensing\n")
    for r in data.get("naming_standards", []) + data.get("licensing_standards", []):
        sections.append(f"### {r['title']}\n\n{r['content']}\n")
    sections.append("## AI governance\n")
    for r in data.get("ai_governance", []):
        sections.append(f"### {r['title']}\n\n{r['content']}\n")
    sections.append("---\n*Canonical source: [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/).*\n")
    return "\n".join(sections)


def write_agents_md(data):
    """Generate dist/AGENTS.md for OpenAI Codex / Jules / OpenCode."""
    (DIST_DIR / "AGENTS.md").write_text(_agents_md_content(data), encoding="utf-8")


def write_claude_md(data):
    """Generate dist/CLAUDE.md for Claude Code."""
    (DIST_DIR / "CLAUDE.md").write_text(_agents_md_content(data), encoding="utf-8")


def write_kiro_steering(data):
    """Generate dist/.kiro/steering/*.md for AWS Kiro."""
    steering_dir = DIST_DIR / ".kiro" / "steering"

    always_parts = []
    for r in data.get("global_rules", []):
        always_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("principles", []):
        always_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (steering_dir / "moj-global.md").write_text(
        "---\ninclusion: always\ndescription: MoJ global rules and development principles\n---\n\n"
        "# MoJ Global Standards\n\n" + "\n".join(always_parts),
        encoding="utf-8",
    )

    coding_parts = []
    for r in data.get("coding_standards", []):
        coding_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("naming_standards", []):
        coding_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("licensing_standards", []):
        coding_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    for r in data.get("ai_governance", []):
        coding_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (steering_dir / "moj-coding-standards.md").write_text(
        "---\ninclusion: always\ndescription: MoJ coding, design, testing, security, naming, licensing and AI governance\n---\n\n"
        "# MoJ Coding and Governance Standards\n\n" + "\n".join(coding_parts),
        encoding="utf-8",
    )

    frontend_parts = []
    for r in data.get("frontend_standards", []):
        frontend_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (steering_dir / "moj-frontend.md").write_text(
        "---\ninclusion: fileMatch\nfileMatchPattern: '**/*.{html,css,scss,tsx,jsx,vue,js,ts}'\n"
        "description: MoJ frontend and accessibility standards\n---\n\n"
        "# MoJ Frontend Standards\n\n" + "\n".join(frontend_parts),
        encoding="utf-8",
    )

    python_parts = []
    for r in data.get("python_standards", []):
        python_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (steering_dir / "moj-python.md").write_text(
        "---\ninclusion: fileMatch\nfileMatchPattern: '**/*.py'\ndescription: MoJ Python-specific standards\n---\n\n"
        "# MoJ Python Standards\n\n" + "\n".join(python_parts),
        encoding="utf-8",
    )

    ruby_parts = []
    for r in data.get("ruby_standards", []):
        ruby_parts.append(f"## {r['title']}\n\n{r['content']}\n")
    (steering_dir / "moj-ruby.md").write_text(
        "---\ninclusion: fileMatch\nfileMatchPattern: '**/*.rb'\ndescription: MoJ Ruby-specific standards\n---\n\n"
        "# MoJ Ruby Standards\n\n" + "\n".join(ruby_parts),
        encoding="utf-8",
    )


def write_human_docs(data):
    """Generate docs/AICE-Standards.md (human-readable reference, stays in this repo)."""
    meta = data.get("meta", {})
    sources = data.get("canonical_sources", [])
    lines = [
        "# MoJ AI Coding Environment (AICE) Standards",
        "",
        "Human-readable reference for Ministry of Justice coding standards, principles, and guidelines used by AI coding tools (Cursor, GitHub Copilot, Claude Code, AWS Kiro, etc.).",
        "",
        f"*Generated from `source/standards.yaml` (version {meta.get('version', 'N/A')}).*",
        "",
        "## Canonical sources",
        "",
        "| Document | Link |",
        "|----------|------|",
    ]
    for s in sources:
        lines.append(f"| {s['title']} | [{s['url'].split('/')[-1] or 'link'}]({s['url']}) |")
    lines.extend([
        "",
        "---",
        "",
        "## Summary of standards and principles",
        "",
        "### Critical (PII and security)",
        "- **Never upload PII** to MoJ GitHub repositories. Keep secrets out of source code.",
        "- Follow MoJ OCTO strategic policies: https://ministryofjustice.github.io/octo-strategic-docs",
        "- [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/)",
        "",
        "### Development principles",
        "- Share knowledge; use GitHub flow; all non-throwaway code reviewed.",
        "- Code: correct (with tests), clear, concise. Optimize for change.",
        "- Something simple that exists beats a perfect solution that doesn't.",
        "- Everything fails: code defensively; fail fast; don't block UX on long external calls.",
        "- Other developers are users: clear code, good commit messages, usable APIs.",
        "- Think smaller: Single Responsibility; small methods; composition over inheritance.",
        "- Names: self-descriptive; avoid puns, obscure acronyms, version numbers in names.",
        "- [Development Principles](https://technical-guidance.service.justice.gov.uk/documentation/principles/development-principles.html)",
        "",
        "### Coding standards",
        "- General: camelCase/PascalCase, max line 120, config not hard-coding, language style guides.",
        "- Version control: GitHub; feature/ branches; commits `type(scope): description`; mandatory review.",
        "- Design: SOLID; versioned APIs; OpenAPI/Swagger; UML for complex systems.",
        "- Technology choices: check the MoJ Technology Radar (https://tech-radar.justice.gov.uk/) before introducing new tools.",
        "- Testing: integration tests for major workflows; automated frameworks; meaningful coverage.",
        "- Security: vulnerability scanning; parameterised queries; input validation; encrypt sensitive data.",
        "- CI/CD: tests on every commit; staging before production; secure config (e.g. Key Vault).",
        "- [Justice Digital software engineering standards](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-software-engineering-standards.html)",
        "",
        "### Frontend and accessibility",
        "- Semantic HTML; ARIA; GOV.UK Design System; WCAG 2.2 AA; keyboard and screen reader testing.",
        "- Responsive design; progressive enhancement; no premature optimisation.",
        "- [Justice Digital front end engineering standards](https://technical-guidance.service.justice.gov.uk/documentation/standards/justice-digital-front-end-engineering-standards.html)",
        "- [Frontend Development Principles](https://technical-guidance.service.justice.gov.uk/documentation/principles/frontend-development-principles.html)",
        "",
        "### Naming",
        "- Self-descriptive names; consistent (e.g. repo name <-> hostname); avoid ambiguous or internal-only acronyms.",
        "- [Naming things](https://technical-guidance.service.justice.gov.uk/documentation/standards/naming-things.html)",
        "",
        "### Licensing",
        "- MIT License; LICENCE or LICENCE.md in each repo; Crown Copyright (Ministry of Justice); proper attribution for reused work.",
        "- [Licensing software or code](https://technical-guidance.service.justice.gov.uk/documentation/standards/licencing-software-or-code.html)",
        "",
        "### AI governance",
        "- Use only MoJ-approved AI tools; no sensitive/PII in AI unless TDA-approved; review all AI output; human in the loop.",
        "- [MOJ Engineering AI Governance Framework](https://technical-guidance.service.justice.gov.uk/documentation/governance/ai-governance-framework.html)",
        "",
        "---",
        "",
        "## How AICE artifacts are built",
        "",
        "Run from the repo root:",
        "",
        "```bash",
        "pip install pyyaml",
        "python scripts/build_aice.py",
        "```",
        "",
        "This generates all artifacts into `dist/`:",
        "- `dist/.cursor/rules/*.mdc`              - Cursor",
        "- `dist/.github/copilot-instructions.md`  - GitHub Copilot / Codex",
        "- `dist/AGENTS.md`                        - OpenAI Codex / Jules / OpenCode",
        "- `dist/CLAUDE.md`                        - Claude Code",
        "- `dist/.kiro/steering/*.md`              - AWS Kiro",
        "",
        "CI/CD can run the same script (see `.github/workflows/build-aice.yml`).",
        "",
    ])
    (DOCS_DIR / "AICE-Standards.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    if not SOURCE_FILE.exists():
        print(f"Source not found: {SOURCE_FILE}", file=sys.stderr)
        sys.exit(1)
    data = load_source()
    ensure_dirs()
    write_cursor_rules(data)
    write_copilot_instructions(data)
    write_agents_md(data)
    write_claude_md(data)
    write_kiro_steering(data)
    write_human_docs(data)
    print("AICE build complete. Artifacts written to dist/:")
    print("  dist/.cursor/rules/*.mdc               (Cursor)")
    print("  dist/.github/copilot-instructions.md   (GitHub Copilot / Codex)")
    print("  dist/AGENTS.md                         (OpenAI Codex / Jules / OpenCode)")
    print("  dist/CLAUDE.md                         (Claude Code)")
    print("  dist/.kiro/steering/*.md               (AWS Kiro)")
    print("  docs/AICE-Standards.md                 (human reference)")


if __name__ == "__main__":
    main()
