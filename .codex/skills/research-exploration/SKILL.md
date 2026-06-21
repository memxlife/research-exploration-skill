---
name: research-exploration
description: Guide disciplined research exploration loops for ambiguous scientific, ML, robotics, computer vision, or algorithm-design work. Use when Codex needs to turn hypotheses into testable claims, design benchmarks, run experiments, inspect visual/quantitative evidence, build or revise experiment result viewers, diagnose failure modes, refine priors or models, write research notes, decide the next experiment, or prepare a subproblem for final paper-style synthesis without drifting into vague speculation.
---

# Research Exploration

Use this skill to keep research work concrete, testable, and evidence-driven.

## Communication Rule

Use simple language. Be precise without using fancy words. Name the concrete
object, variable, file, metric, stage, example, or decision being discussed.
Do not use buzzwords, project nicknames, vague abstractions, or compressed
phrases when a concrete description is possible.

When explaining a result, say:

```text
what was tested
where the evidence is
what passed
what failed
why it failed, if known
what the next concrete test is
```

Do not use polished research language to hide an unclear idea. If a term is
important, define it as a test or computation.

For visualization and result analysis, do not try to save words. The purpose of
the viewer is to provide feedback that helps the researcher understand the
problem structure. Each result should explain enough context for a careful
undergraduate reader to understand what was measured, how to read it, what was
observed, and what conclusion is allowed.

## Result-First Rule

When the user asks for a concrete experimental result, number, accuracy, loss,
metric, status, or comparison, return the direct first-hand result as soon as it
is available. Do not delay the answer in order to polish the viewer, update a
document, reorganize files, or add extra analysis.

Research is an iterative exploration process. Fast turnaround is part of the
method, not a convenience. Prefer the shortest reliable measurement that can
answer the current question, report it immediately, and only then decide whether
larger experiments, cleaner plots, or deeper documents are worth the time.

For experiment questions, use this order:

```text
1. get the minimal measurement needed to answer the question
2. report the first-hand result immediately
3. then refine visualization, documents, interpretation, or follow-up analysis
```

If the result is already known from a completed command, JSON file, log, or
viewer artifact, answer with the number first. Then mention where the result
came from and whether a caveat matters. Only after that should you propose or
perform viewer/document cleanup.

Learning should have no barrier. When presenting experimental results, write
patiently. Do not assume the reader remembers the conversation, knows why a
metric matters, or can infer the lesson from a table. For each important result,
include the missing bridge between the number and the conclusion:

```text
what the model/data looked like in plain language
what the metric means before showing the value
what value would be expected if the hypothesis were true
what value would be expected if the hypothesis were false
the actual values
how to compare the values
the narrow conclusion from that comparison
what a student should remember
```

Avoid compressed phrases such as "confirms the mechanism" unless the mechanism
has just been restated in plain language. Prefer concrete sentences like:
"The rare example learned later because the common update pointed partly toward
the wrong answer." Do not use unexplained labels, abbreviations, or shorthand.
If a table has more than three columns of metrics, explain each metric before
the table and tell the reader which one to inspect first.

Do not rely on repeated post-hoc checking to rescue unclear visualization work.
The viewer should be designed from explicit plot contracts before code is
written. Verification is still required, but it must be bounded: render once,
inspect against the audit checklist, fix concrete failures, and stop when the
viewer satisfies the contract. Do not spend research time repeatedly refreshing
or manually checking a viewer whose plot definitions were never made clear.

## Core Rule

Do not treat a plausible idea as progress. Progress requires:

```text
hypothesis -> operational definition -> minimal test -> metric + visual evidence -> failure analysis -> refined hypothesis
```

Research progress is conjecture refinement through falsification:

```text
conjecture -> rigorous falsification -> problem-structure discovery -> updated conjecture
```

A failed experiment is useful only when it reveals which assumption, stage, or
prior was wrong. A successful experiment is useful only when it explains why the
result succeeded.

Repeated failure can also mean the goal is wrong. If several precise algorithms
fail in the same way, stop and ask whether the target label, metric, or success
condition matches the downstream purpose.

## Required Chain

For nontrivial research work, keep this chain inspectable:

```text
conjecture -> physical priors -> mathematical model -> implementation contract -> experiment -> failure analysis -> updated conjecture
```

The document should not be only a log. It should show how each prior becomes a
model, how each model becomes code, and how experiments can falsify or refine
the conjecture.

## Required Artifacts

Do not deliver a final research answer unless the notes, report, or response
contain:

```text
falsifiable conjecture
physical priors
mathematical model for each prior
implementation contract for each model
publication-grade experimental setup
explicit algorithm specification for each nontrivial stage
stage-level profiling evidence
failure interpretation for each stage
conjecture update or next uncertainty
claim boundary
```

If an artifact is missing, say the research state is incomplete and name the
missing artifact.

When a self-contained subproblem reaches a stable conclusion, automatically use
the sibling `research-final-report` skill to create `docs/final_report.md`.
This final report is required before treating the subproblem as closed. The
final report is a synthesis article, not another experiment log.

## Subproblem Document Standard

For each self-contained research subproblem, create or maintain exactly these
three primary working documents unless the user requests a different structure:

```text
docs/design.md
  problem definition, physical priors, math model, and computation contract

docs/experiment_design.md
  detailed falsification and profiling plan, including pass/fail/insufficient
  evidence conditions

docs/visualization_results.md
  problem-specific viewer description, actual experiment results, how to read
  each result, observed result, take-home conclusion, and remaining uncertainty
```

After the subproblem reaches a stable conclusion, create a fourth synthesis
document:

```text
docs/final_report.md
  final paper-style report that merges problem formulation, physical priors,
  mathematical modeling, computational implementation, experiment design,
  results, analysis, claim boundary, conclusion, and next research question
```

Use `docs/final_report.md` only after the working documents and evidence are
stable enough to tell the whole story end to end. It should be rigorous,
student-readable, and self-contained. A new reader should not need the chat
history, raw logs, or private context to understand the subproblem.

The visualization/results document is not a screenshot dump. It must explain
what each plot proves, what it does not prove, and how the viewer supports the
current claim boundary.

Every research report and viewer must include a dedicated experimental setup
section before the result plots. This section should read like the experiment
setup section of a research paper, not like a short caption. It must define the
objects being compared before any result label uses them.

The setup section must include, when applicable:

```text
research question
dataset construction or data-generating process
train/validation/test split or probe set
model architecture
input representation and position encoding
loss function
optimizer or update rule
training steps, tokens, batch size, and checkpoint interval
random seed and deterministic/stochastic choice
all conditions being compared, with plain-language labels
which variables are changed between conditions
which variables are held fixed
metric definitions, units, and thresholds
script path and output artifact path
known limitations of the setup
```

If a condition name appears in a plot or table, it must be defined in the setup
section before the plot. Labels like "orthogonal conflict" or "strong overlap"
are not self-explanatory unless the page states the exact values and plain
meaning.

The same standard applies to the viewer itself. Every visible plot should carry
its own explanation. A plot caption that only says "higher is better" is not
enough. State the exact comparison, the metric definition, the axis meaning, the
observed numbers or pattern, and the take-home conclusion. If the plot cannot be
explained clearly, remove it from the main viewer.

## Quick Workflow

1. State the claim in one falsifiable sentence.
2. Separate the physical prior, math model, algorithm, and experiment.
3. Define important terms as tests, including success, failure, and insufficient evidence.
4. Write the exact algorithm before running the experiment.
5. Build the smallest diagnostic benchmark or micro-test.
6. Measure both numbers and visual evidence.
7. Inspect stage-level evidence before changing the algorithm.
8. Decompose broad failures into smaller tests.
9. Audit the goal when repeated reasonable fixes fail.
10. Update the current-state document and the iteration ledger.
11. When the subproblem reaches a stable conclusion, use `research-final-report`
    to create `docs/final_report.md`.

## Non-Negotiable Rules

Do not run an experiment against a hand-waved algorithm. For any nontrivial
algorithm, first write:

```text
input
parameters
intermediate variables
step-by-step procedure
pass conditions
fail conditions
failure reasons
outputs
debug artifacts
```

Do not debug only the final output of a pipeline. Each stage must expose enough
evidence to explain why examples pass, fail, or become uncertain before the next
stage consumes them.

Do not stop at a yes/no outcome. The "why" comes from stage-level profiling:

```text
stage -> artifact -> pass/fail criteria -> representative examples -> next-stage handoff
```

When an experiment fails, say whether it falsified the physical prior itself or
only one operationalization of that prior.

When observations unfold over time or changing conditions, do not replace that
with a single-observation proxy unless the proxy itself is being tested.

For slow research loops, run a fast micro-test first. Use known good and bad
examples, a small number of observations or cases, and stage-local artifacts.

## Non-Negotiable Viewer Rule

Every plot in a research viewer must pass a self-explanation audit before it is
shown to the user. This is a MUST rule, not a style preference.

Before adding or keeping any visible plot, evaluate it as if the reader has not
seen the conversation, code, metric implementation, or prior plots. The plot is
allowed in the main viewer only if a careful undergraduate reader can answer all
of these from the visible page:

```text
what question this plot answers;
the exact metric definition, including formula and unit;
what data produced the plot;
what each axis, color, bar, line, point, or legend item means;
which direction is better, worse, larger, smaller, or more stable;
the key observed numbers or pattern;
the narrow conclusion supported by this plot;
what the plot does not prove.
```

If any item is missing, do not show the plot. Rewrite it, split it into simpler
plots, add a metric definition table, add direct numeric labels, or move it to a
debug appendix explicitly marked as not supporting the current conclusion.

Do not combine metrics with different units on one axis. Do not rescale one
metric to make it fit beside another unless the viewer states the transformation
in the plot title, axis label, legend, and explanation. Prefer separate plots
when two metrics answer different questions.

For every viewer update, perform and report a self-explanation audit before the
final answer. If the plot is still hard to explain in plain language, remove it.

## Viewer Harness Requirement

For research viewers, the agent must use a harness that prevents unclear plots
from being delivered. The harness has five required gates:

```text
Gate 1: Plot contract before plotting
Gate 2: Self-explanatory viewer implementation
Gate 3: Bounded rendered artifact audit after plotting
Gate 4: Stable local serving for browser-based viewers
Gate 5: Independent review before delivery, when delegation tools are available
  and tool policy permits their use
```

Gate 1 requires a plot contract for every planned plot:

```text
plot title
research question answered
metric name
metric formula
metric unit
data source
aggregation level
x-axis meaning
y-axis meaning
legend meaning
allowed conclusion
known limitation
```

Do not implement the plot until the contract is clear. If the metric cannot be
defined in one or two plain sentences plus a formula when needed, the metric is
not ready to plot.

Gate 2 requires building the visible explanation into the viewer itself. Do not
put the real interpretation only in the final chat response or in source-code
comments. For each plot, the visible page must include:

```text
purpose
exact setup
metric definition
how to read axes, colors, signs, and groups
observed result with concrete numbers when available
take-home conclusion
what the plot does not prove, if important
```

Gate 3 requires a bounded rendered artifact audit. The agent must inspect the
generated viewer, not only the source code. This audit is a finite checklist,
not an open-ended manual debugging loop. The audit must check:

```text
page renders
no raw LaTeX is visible unless that is intended
legend is not clipped
axis labels are readable
units are visible
metric definitions appear before plots
each plot has one primary unit on the y-axis
important numbers are shown in text or a table near the plot
the plot can be explained without reading code
```

Gate 4 requires stable local serving for browser-based viewers. A research
viewer should not depend on an ad-hoc shell process that dies after the turn.
For static viewers, prefer a durable local HTTP server with a stable port and a
restart command recorded in the project. Use the helper script in this skill
when appropriate:

```text
scripts/ensure_static_viewer_server.sh
```

The final answer must include the stable URL and a command that checks or
restarts the server.

Gate 5 requires independent review when possible. If multi-agent or reviewer
tools are available and the current tool policy permits delegation, spawn or
ask an independent reviewer to inspect the viewer for reader confusion before
delivery. The reviewer task must be concrete:

```text
Read the rendered viewer as a new reader.
List any undefined metric, mixed unit, clipped legend, unclear axis, unsupported
conclusion, or plot that requires code knowledge.
Approve only if every plot is self-explanatory.
```

If no independent reviewer can be used, the agent must run the same checklist
itself and explicitly say that no independent reviewer was used.

The output of the harness must be recorded in the project, for example in:

```text
docs/viewer_audit.md
```

The final response after viewer work must include:

```text
where the audit is recorded
whether independent review was used
which plots were changed or removed
which metric definitions were added
what the viewer now supports
what remains uncertain
```

## Reference Files

Load only the reference file needed for the task:

- `references/algorithm_specification.md`: when an algorithm has multiple steps, thresholds, matching, clustering, fitting, ranking, or hidden heuristics.
- `references/profiling_and_evidence.md`: when planning experiments, running tests, reviewing results, or deciding what evidence is missing.
- `references/failure_decomposition.md`: when a failure is broad, confusing, or could have several causes.
- `references/goal_audit.md`: when several reasonable fixes fail, when labels may not match the downstream purpose, or when false positives and false negatives have different costs.
- `references/research_documentation.md`: when writing or revising a research document, design note, experiment note, or iteration ledger.
- `references/research_viewer_design.md`: when creating or revising an experiment visualization viewer, dashboard, HTML report, or plot set.
- `references/research_loop_checklist.md`: when a short checklist is enough for planning or review.

## Local Viewer Server Reliability

When the user is using an in-app browser or asks to see results in a viewer,
the viewer URL must be stable enough for iterative research. Do not leave the
user with a page that only works while a temporary terminal command is alive.

For static HTML viewers, use one of these serving modes:

```text
Preferred for repeated research work:
  a macOS LaunchAgent created by scripts/ensure_static_viewer_server.sh

Acceptable for a one-off check:
  a foreground or tmux server, with the command shown to the user

Avoid:
  a background process started with shell job control and no restart policy
```

For each project, keep one stable port when possible. Record the URL and restart
command in the result document or viewer audit. If a port changes, state the
new URL explicitly.

Before telling the user the viewer is ready, run a bounded server check:

```text
HTTP status is 200
the expected index.html is being served
the server has a restart policy or a documented restart command
```

## Writing Standard

Use concise causal structure:

```text
Objective and conclusion
1. Physical modeling
2. Mathematical modeling
3. Computational implementation and results
```

Every equation must map to a physical prior and a code path. Every
hyperparameter must have a name, value, definition, reason for the value, and
expected effect when it is too low or too high when that effect matters.

Write simply. Rigor means precise, not fancy. A reader should be able to
implement the algorithm from the document without guessing.
