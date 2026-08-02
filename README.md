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
- one authoritative design document per active research question, with linked
  experiment-control details only when execution requires them.

## Research Question Standard

For a single question, `node-dir` is `docs/`. For a mapped hierarchy, read each
question's `node-dir` from `docs/research_map.md`. Every active question owns
one authoritative design document:

```text
<node-dir>/design.md
```

For a material-literature child question, the canonical design has six parts:

1. Problem Definition.
2. Physical Priors.
3. Mathematical Model.
4. Related Work and Computational Design Decisions.
5. Computational Implementation.
6. Experiments and Iterative Evidence.

A routine fixed question may use the documented reduced four-part form when the
literature gate does not trigger. The skill defines section ownership,
mathematical-problem, learned-model, constructible-computation, evidence, and
plain-language completion gates for both forms.

When researcher input, causal reasoning, or evidence makes a child question
active, it becomes the center of a new recursive research unit. Do not generate
a large question tree upfront.

For a multi-question program, use stable node IDs and place an activated child
under `docs/problems/<ID>/`. The parent design links the child and records its
relationship; do not create empty child documents or a competing source of
research truth.

```text
<node-dir>/experiment_design.md
```

Detailed experiment-control design for falsification and profiling. Use this
companion only when execution requires protocol, command, schema, receipt, or
resource detail that would obscure the design. The main design still records
each round's scientific question, setup, data, result, interpretation, claim
boundary, and next decision.

```text
<node-dir>/visualization_results.md
```

Optional problem-specific viewer description when visual diagnosis is
material. It is not a mandatory document for an early design or a NOT RUN
round.

When visual evidence is required, the viewer is part of the research method.
Every plot should be readable by a careful undergraduate without reading the
source code or remembering prior conversation.

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
.codex/skills/research-exploration/scripts/check_markdown_math.py
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
