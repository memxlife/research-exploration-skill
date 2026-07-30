# Research Exploration Skill

Codex skill for disciplined research exploration loops in ambiguous scientific,
machine learning, robotics, computer vision, and algorithm-design work.

The skill emphasizes:

- research-question-first inspiration,
- physical priors as conjectures about problem structure,
- mathematical and computational realization of those priors,
- falsification and profiling that improve structural understanding,
- operational definitions,
- smallest diagnostic benchmarks,
- metrics plus visual evidence,
- stage-by-stage debugging for multi-step algorithms,
- verified failure analysis before adding complexity,
- evidence-driven recursive question refinement,
- self-contained research-question documentation with three primary documents:
  `docs/design.md`, `docs/experiment_design.md`, and
  `docs/visualization_results.md`.

## Research Question Standard

For a single question, `node-dir` is `docs/`. For a mapped hierarchy, read each
question's `node-dir` from `docs/research_map.md`. Every active question should
maintain three documents:

```text
<node-dir>/design.md
```

The current research unit in four parts:

1. Problem Definition, centered on the current research question and its
   importance, parent, child questions, relations, bounded answer, and frontier.
2. Physical Priors, including the conjectured structure and predicted
   observable consequence.
3. Mathematical Model derived from the selected prior or coupled priors.
4. Computational Implementation for falsification and profiling.

When researcher input, causal reasoning, or evidence makes a child question
active, it becomes the center of a new recursive four-part research unit. Do
not generate a large question tree upfront.

For a multi-question program, maintain `docs/research_map.md` and use stable
node IDs with working documents and `iterations.md` ledgers under
`docs/problems/<ID>/`. Existing root documents may remain mapped to `P0`.
The research map owns the program frontier and shared coupled-set contracts. A
frontier may contain a coupled set when its questions cannot be interpreted
independently.

```text
<node-dir>/experiment_design.md
```

Detailed experiment design for falsification and profiling. Profiling evidence
must explain why a result passed, failed, or remained uncertain.

```text
<node-dir>/visualization_results.md
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

During `npm install`, the package automatically links both cooperating skills:

```text
~/.codex/skills/research-exploration
~/.codex/skills/research-final-report
```

If either skill already exists, the installer leaves that copy unchanged. To
replace existing local copies with source links:

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
.codex/skills/research-exploration/references/problem_refinement.md
.codex/skills/research-exploration/references/research_documentation.md
.codex/skills/research-exploration/references/research_loop_checklist.md
.codex/skills/research-exploration/scripts/build_iclr_paper.sh
.codex/skills/research-final-report/SKILL.md
scripts/install-codex-skill.mjs
```

The packaged directories under `.codex/skills/research-exploration` and
`.codex/skills/research-final-report` are the sources of truth. Their Codex
runtime paths should be symlinks to these directories, so the skills used by
Codex are the same copies tracked by Git.

Platform-specific local tools such as `.codex/skills/research-exploration/tools/tectonic`
remain untracked. The LaTeX build helper uses that local executable when
present, then falls back to `tectonic` from `PATH`.

## Validate

```bash
npm run check
npm pack --dry-run
```
