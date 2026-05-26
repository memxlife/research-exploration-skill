---
name: research-exploration
description: Guide disciplined research exploration loops for ambiguous scientific, ML, robotics, computer vision, or algorithm-design work. Use when Codex needs to turn hypotheses into testable claims, design benchmarks, run experiments, inspect visual/quantitative evidence, diagnose failure modes, refine priors or models, write research notes, or decide the next experiment without drifting into vague speculation.
---

# Research Exploration

Use this skill to keep research work causal, testable, and evidence-driven.

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

Research documentation is part of the falsification machinery. For nontrivial
research problems, write the research object so the causal chain is inspectable:

```text
conjecture -> physical priors -> mathematical model -> implementation contract -> experiment -> failure analysis -> updated conjecture
```

The document should not be a log. It should show how each prior becomes a model,
how each model becomes code, and how experiments can falsify or refine the
conjecture.

Do not stop at a yes/no outcome. The "why" comes from stage-level profiling:
break the task into physical priors, mathematical modeling steps, computation
stages, evidence at each stage, and the failure interpretation for each stage.

For multi-step algorithms, progress also requires inspectable intermediate
outputs:

```text
stage -> artifact -> pass/fail criteria -> representative examples -> next-stage handoff
```

Do not debug only the final output of a pipeline. Each stage must expose enough
evidence to explain why examples pass, fail, or become uncertain before the next
stage consumes them.

For large failures, falsification is recursive decomposition. Do not ask only
"why did the whole system fail?" Break the failure into smaller sub-problems,
test each sub-problem, and keep decomposing until the true bottleneck becomes
local, observable, and fixable:

```text
big failure -> sub-problems -> stage-local tests -> verified bottleneck -> targeted fix
```

Each decomposition level must produce an answer, even if that answer is "not the
cause." Negative answers are progress because they remove false explanations.

## Enforcement Standard

For nontrivial research work, do not deliver a final research answer unless the
following artifacts exist in the notes, report, or response:

```text
falsifiable conjecture
physical priors
mathematical model for each prior
implementation contract for each model
stage-level profiling evidence
failure interpretation for each stage
conjecture update or next uncertainty
claim boundary
```

If any artifact is missing, say that the research state is incomplete and name
the missing artifact. Do not replace missing evidence with confident narrative.

For each stage in a multi-step algorithm, enforce this minimum audit:

```text
question: what is this stage supposed to prove or falsify?
input evidence: what entered the stage?
output evidence: what was accepted, rejected, or uncertain?
failure evidence: what failed and by which reason?
artifact: what file, plot, table, screenshot, or viewer state lets a human inspect it?
interpretation: what does this stage imply for the conjecture?
```

The final yes/no answer must be backed by the causal path:

```text
final result -> stage evidence -> bottleneck or support -> conjecture update
```

## Workflow

### 1. State The Claim

Write the claim in one sentence. Make it falsifiable.

Prefer:

```text
Distinctive early-layer visual anchors can be triangulated into persistent 3D points under known egocentric motion.
```

Avoid:

```text
The model understands 3D structure.
```

### 2. Separate Prior, Math, And Implementation

Keep three layers aligned.

```text
physical prior: what must be true in the world
mathematical model: how that prior is represented and tested
implementation: exact code path, parameters, data, and outputs
```

If the implementation has a heuristic that is not in the prior or math, either
remove it or explicitly name it as an implementation heuristic.

### 3. Define Each Term Operationally

Do not leave important words intuitive. Define them as tests.

Examples:

```text
stable: target descriptor remains similar across frames
distinctive: few nearby or epipolar candidates have similar descriptors
persistent: repeated positive support creates one 3D hypothesis
missing: no usable match; neutral evidence, not deletion
ambiguous: too many plausible matches; invalid for 3D promotion
boundary: sparse anchor with missing local 3D support on one side
```

### 4. Build The Smallest Diagnostic Benchmark

Design the benchmark to isolate one claim.

Require:

```text
known controllable setup
clear ground truth for the tested concept
enough variation to expose the prior
simple visual patterns that humans can inspect
failure cases that are easy to interpret
```

Change the benchmark when it cannot answer the question.

### 5. Run The Conjecture Refinement Loop

After each experiment, explicitly record:

```text
original conjecture
expected evidence if true
falsification test
what survived
what failed
hidden problem structure revealed
updated conjecture
next uncertainty to isolate
```

Do not merely report whether the experiment worked. Use falsification to make
the next conjecture more physically, mathematically, and computationally
appropriate.

For multi-step systems, record both the final answer and the causal path:

```text
final yes/no -> stage evidence -> bottleneck or support -> conjecture update
```

### 5.5 Write The Research Object As A Testable Argument

When a research problem becomes more than a quick experiment, write a concise
design document that regularizes the loop:

```text
conjecture
task input and output
core difficulty
physical priors
mathematical model for each prior
implementation stage for each model
experiment that can falsify the priors
conjecture update from the result
```

Use a consistent subsection format when helpful:

```text
Objective: what this part tries to do
Physical prior: why this step is plausible in the world
Model: the equation or formal representation
Implementation contract: the code stage, inputs, outputs, and pass/fail checks
Evidence: metrics, visual examples, and failure cases
```

For experiments, add a stage-level falsification and profiling plan:

```text
Question: what does this stage need to prove or falsify?
Model and implementation: which prior, equation, and code stage are tested?
Profiling evidence: what counts, distributions, visual examples, and timings are collected?
Failure interpretation: what does each failure mode mean for the conjecture?
```

The writing standard is simple: every claim should connect to a prior, every
prior should connect to a model, every model should connect to implementation,
and every implementation should be falsifiable by experiment.

### 6. Recursively Decompose Failures

When the failure is broad or confusing, turn it into a hierarchy of smaller
questions before changing the algorithm.

For each decomposition level, record:

```text
parent failure
candidate sub-problems
test for each sub-problem
answer for each sub-problem
evidence supporting each answer
remaining bottleneck
```

Use this pattern:

```text
Is the viewer wrong?
Is the benchmark missing the target behavior?
Are candidates missing?
Is the correct match outside the search region?
Is matching ambiguous?
Is geometry rejecting correct matches?
Is final promotion too permissive?
```

The exact questions depend on the domain, but the rule is general: a big failure
is solved by recursively isolating which sub-problem is actually false.

Only change the algorithm after the decomposition identifies a specific failed
sub-problem. If multiple sub-problems remain plausible, instrument them first.

### 7. Measure And Look

Every experiment needs both numbers and visual evidence.

Minimum report:

```text
purpose
setup
parameters
metrics
good examples
bad examples
visualization of the current state
interpretation
next experiment
```

For spatial or vision work, include frame-by-frame or interactive 3D
visualization whenever possible.

### 8. Instrument Multi-Step Algorithms

When the algorithm has multiple stages, treat each stage as a falsifiable
sub-task. Before trusting the full pipeline, create stage-local diagnostics.

Before implementing or trusting each stage, write a stage contract:

```text
input assumptions
sub-task objective
expected intermediate output
pass/fail criterion
debug artifact
representative pass examples
representative fail examples
next-stage handoff contract
```

After running the stage, record runtime evidence against that contract:

```text
input count and distribution
accepted output count and distribution
rejected output count by reason
intermediate artifacts saved to disk
```

For frame/sequence/spatial algorithms, include per-frame or per-region debug
views, not just aggregate metrics.

Example:

```text
candidate features -> matched observations -> triangulated points -> merged anchors -> surface regions
```

Each arrow must have debug evidence. If final anchors fail, inspect candidate
selection, matching, triangulation, merge, and promotion separately before
changing the model.

### 9. Diagnose Failures Before Adding Complexity

Classify failures before changing the algorithm.

Common categories:

```text
wrong prior
unclear term definition
bad benchmark
bad ground truth
insufficient visualization
implementation bug
hyperparameter mismatch
model limitation
```

Prefer one targeted change over many simultaneous changes.

### 10. Record The Research State

End each loop with:

```text
what is validated
what failed
what remains uncertain
what changed in the hypothesis
what the next test should isolate
```

Be explicit about claim boundaries. Do not call sparse anchors a dense surface
model. Do not call boundary candidates object segmentation unless that was
tested.

When a failure is found in a multi-stage pipeline, say exactly which stage is
verified as the bottleneck and which alternative explanations were falsified.

When a recursive decomposition resolves a problem, record the final causal path:

```text
big failure -> falsified explanations -> verified bottleneck -> fix -> remaining unsolved problem
```

## Writing Research Documents

Use concise causal structure:

```text
Objective and conclusion
1. Physical modeling
2. Mathematical modeling
3. Computational implementation and results
```

Every mathematical equation must map to a physical prior and a code path.
Every hyperparameter must have:

```text
name
value
definition
reason for this value
effect if too low or too high, when useful
```

## Extra Checklist

For detailed checklists, read `references/research_loop_checklist.md` only when
the task needs experiment planning, report review, or methodology auditing.
