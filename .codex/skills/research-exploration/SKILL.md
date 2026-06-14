---
name: research-exploration
description: Guide disciplined research exploration loops for ambiguous scientific, ML, robotics, computer vision, or algorithm-design work. Use when Codex needs to turn hypotheses into testable claims, design benchmarks, run experiments, inspect visual/quantitative evidence, build or revise experiment result viewers, diagnose failure modes, refine priors or models, write research notes, or decide the next experiment without drifting into vague speculation.
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
explicit algorithm specification for each nontrivial stage
stage-level profiling evidence
failure interpretation for each stage
conjecture update or next uncertainty
claim boundary
```

If an artifact is missing, say the research state is incomplete and name the
missing artifact.

## Subproblem Document Standard

For each self-contained research subproblem, create or maintain exactly these
three primary documents unless the user requests a different structure:

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

The visualization/results document is not a screenshot dump. It must explain
what each plot proves, what it does not prove, and how the viewer supports the
current claim boundary.

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

## Reference Files

Load only the reference file needed for the task:

- `references/algorithm_specification.md`: when an algorithm has multiple steps, thresholds, matching, clustering, fitting, ranking, or hidden heuristics.
- `references/profiling_and_evidence.md`: when planning experiments, running tests, reviewing results, or deciding what evidence is missing.
- `references/failure_decomposition.md`: when a failure is broad, confusing, or could have several causes.
- `references/goal_audit.md`: when several reasonable fixes fail, when labels may not match the downstream purpose, or when false positives and false negatives have different costs.
- `references/research_documentation.md`: when writing or revising a research document, design note, experiment note, or iteration ledger.
- `references/research_viewer_design.md`: when creating or revising an experiment visualization viewer, dashboard, HTML report, or plot set.
- `references/research_loop_checklist.md`: when a short checklist is enough for planning or review.

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
