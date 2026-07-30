# LaTeX Toolchain

The build helper first looks for a skill-local Tectonic compiler at:

```text
tools/tectonic
```

If that file is absent, it uses `tectonic` from `PATH`. The platform-specific
compiler binary is intentionally not stored in Git.

For an ICLR paper whose source is `paper/main.tex`, run from the project root:

```bash
~/.codex/skills/research-exploration/scripts/build_iclr_paper.sh paper
```

The script keeps the LaTeX log and intermediate files so equation, citation,
page-count, and overflow warnings can be audited. A skill-local compiler does
not modify the shared Python environment or require a system-wide MacTeX
installation.
