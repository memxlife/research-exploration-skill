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

## Install With npm

Install from the repository:

```bash
npm install -g .
```

During `npm install`, the package automatically installs the skill to:

```text
~/.codex/skills/research-exploration
```

If the skill already exists, the installer leaves it unchanged. To replace an
existing local copy:

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

The packaged skill under `.codex/skills/research-exploration` is the install
source of truth.

## Validate

```bash
npm run check
npm pack --dry-run
```
