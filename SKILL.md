---
name: research-exploration
description: Guide disciplined research exploration loops for ambiguous scientific, ML, robotics, computer vision, or algorithm-design work. Use when Codex needs to turn hypotheses into testable claims, design benchmarks, run experiments, inspect visual/quantitative evidence, diagnose failure modes, refine priors or models, write research notes, or decide the next experiment without drifting into vague speculation.
---

# Research Exploration

Use this skill to keep research work causal, testable, and evidence-driven.

## Communication Rule

Keep the conversation concrete and simple. Name the specific object, variable,
file, metric, frame, stage, or decision being discussed. Avoid vague phrases
such as "the signal," "the approach," or "the thing" when a concrete name is
available.

Use short sentences. Prefer plain words over jargon. If a technical term is
needed, define it as a test or a computation. Do not use polished-sounding
research language to cover an unclear idea.

When explaining a result, say:

```text
what was tested
what file or artifact contains the evidence
what passed
what failed
why it failed, if known
what the next concrete test is
```

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

Do not run an experiment against a hand-waved algorithm. For any nontrivial
algorithm, first write an executable specification in simple words:

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

The algorithm is part of the research claim. If the algorithm is vague, the
experiment cannot falsify the conjecture because nobody knows what was tested.

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
explicit algorithm specification for each nontrivial implementation stage
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
A measurable signal remains stable under specified perturbations and predicts the target label above a defined threshold.
```

Avoid:

```text
The model understands the hidden structure.
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

Before coding or running a benchmark, check the alignment in plain language:

```text
physical prior:
  what should happen in the world?
math model:
  what variables measure that thing?
algorithm:
  what exact steps compute those variables?
experiment:
  what result would support or falsify the model?
```

If the algorithm cannot be written as exact steps, stop and specify it first.
Do not hide unclear reasoning behind words like "cluster," "match,"
"consistent," "stable," "local," or "valid." Define the exact test.

Before choosing an experiment, list the plausible physical parameters that
could operationalize the prior. If a key construct can be interpreted in more
than one way, name the competing interpretations instead of silently choosing
one.

When observations unfold over time or under changing conditions, distinguish:

```text
instantaneous evidence: what is true in one observation
temporal evidence: what persists or changes across observations
structural evidence: what is true after aggregating observations into a higher-level representation
```

Do not replace a temporal or structural parameter with an instantaneous proxy
unless that simplification is explicitly the thing being tested.

### 3. Define Each Term Operationally

Do not leave important words intuitive. Define them as tests.

Examples:

```text
stable: target descriptor remains similar across frames
distinctive: few nearby or epipolar candidates have similar descriptors
persistent: repeated positive support creates one 3D hypothesis
missing: no usable match; neutral evidence, not deletion
ambiguous: too many plausible matches; invalid for 3D promotion
valid: evidence satisfies the acceptance rule for the current stage
```

For each operational definition, include the negative case:

```text
what counts as success?
what counts as failure?
what counts as insufficient evidence?
which failure reason is recorded?
```

This matters because "no" is not enough. The research loop needs to know why
the answer is no.

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
candidate physical parameters considered
chosen operationalization
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

When an experiment fails, say whether it falsified the physical prior itself or
only one operationalization of that prior. A failed simple proxy may strengthen
the case for a temporal or structural parameter rather than invalidating the
original idea.

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

Separate current theory from research provenance:

```text
current-state document:
  the latest clean problem definition, priors, model, implementation contract,
  falsification plan, claim boundary, and current uncertainty;

iteration ledger:
  the append-only sequence of conjecture -> operationalization -> profiling ->
  result -> interpretation -> conjecture update.
```

The current-state document should be rewritten as understanding improves. The
iteration ledger should preserve how that understanding changed. Do not bury
old failed operationalizations inside the current model; keep them in the
ledger as evidence about what was falsified and why.

Use a consistent subsection format when helpful:

```text
Objective: what this part tries to do
Physical prior: why this step is plausible in the world
Model: the equation or formal representation
Implementation contract: the code stage, inputs, outputs, and pass/fail checks
Evidence: metrics, visual examples, and failure cases
```

For algorithm-heavy sections, use an explicit procedure block:

```text
Algorithm:
1. Read these inputs.
2. Compute these intermediate variables.
3. Apply this decision rule.
4. If the rule fails, record this failure reason.
5. Save these outputs and debug artifacts.
```

Every parameter in the procedure must have a name, value, meaning, and expected
effect when it is too small or too large.

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

For each iteration, use this minimum record:

```text
Conjecture: what is currently believed.
Physical parameterization: which measurable version of the idea is being tested.
Operationalization: how the parameterization becomes variables, thresholds, or stages.
Profiling plan: what intermediate evidence will explain success or failure.
Result: metrics, artifacts, and representative examples.
Interpretation: what succeeded, what failed, and why.
Conjecture update: what changes in the current-state document.
Next uncertainty: the smallest remaining uncertainty to isolate.
```

If an experiment tests only one possible operationalization of a broader prior,
say that explicitly. A failed proxy should not be written as a failed prior
unless the profiling evidence rules out the broader prior.

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
exact algorithm steps
expected intermediate output
pass/fail criterion
named failure reasons
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

For slow research loops, make a fast micro-test first. Use already-known good
and bad examples, a small number of frames or cases, and stage-local artifacts.
Full sweeps are useful only after the fast test shows the operationalization is
worth scaling.

Example:

```text
candidate generation -> matching -> estimation -> merging -> final prediction
```

Each arrow must have debug evidence. If the final prediction fails, inspect
candidate generation, matching, estimation, merging, and promotion separately
before changing the model.

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

Be explicit about claim boundaries. Do not describe an intermediate artifact as
a complete model, and do not claim a task was solved unless that exact task was
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

Write simply. Rigor means precise, not fancy. Prefer short sentences and common
words. Avoid jargon unless it is defined as a concrete test. A reader should be
able to implement the algorithm from the document without guessing.

## Extra Checklist

For detailed checklists, read `references/research_loop_checklist.md` only when
the task needs experiment planning, report review, or methodology auditing.
