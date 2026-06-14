# Research Exploration Skill

Codex skill for disciplined research exploration loops in ambiguous scientific,
machine learning, robotics, computer vision, and algorithm-design work.

The skill emphasizes:

- falsifiable hypotheses,
- operational definitions,
- smallest diagnostic benchmarks,
- metrics plus visual evidence,
- stage-by-stage debugging for multi-step algorithms,
- verified failure analysis before adding complexity.
- self-contained subproblem documentation with three primary documents:
  `docs/design.md`, `docs/experiment_design.md`, and
  `docs/visualization_results.md`.

## Research Subproblem Standard

Each self-contained research subproblem should maintain three documents:

```text
docs/design.md
```

Problem definition, physical priors, mathematical model, and computation
implementation contract.

```text
docs/experiment_design.md
```

Detailed experiment design for falsification and profiling. Profiling evidence
must explain why a result passed, failed, or remained uncertain.

```text
docs/visualization_results.md
```

Problem-specific viewer description and actual results. Each result should
state the problem being tested, exact setup, observed result, take-home
conclusion, and claim boundary.

The viewer is part of the research method. Every plot should be readable by a
careful undergraduate without reading the source code or remembering prior
conversation.

## Install With npm

Install from the repository:

```bash
npm install -g .
```

During `npm install`, the package automatically links the skill to:

```text
~/.codex/skills/research-exploration
```

If the skill already exists, the installer leaves it unchanged. To replace an
existing local copy with a source link:

```bash
RESEARCH_EXPLORATION_UPDATE_SKILL=1 npm install -g .
```

After this project is published to GitHub, install directly from the repository:

```bash
npm install -g github:memxlife/research-exploration-skill
```

## Layout

```text
.codex/skills/research-exploration/SKILL.md
.codex/skills/research-exploration/agents/openai.yaml
.codex/skills/research-exploration/references/research_loop_checklist.md
scripts/install-codex-skill.mjs
```

The packaged skill under `.codex/skills/research-exploration` is the only
source of truth. The Codex runtime path should be a symlink to this directory,
so the skill used by Codex is the same copy that is tracked by Git.

## Validate

```bash
npm run check
npm pack --dry-run
```
