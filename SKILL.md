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
prior was wrong.

For multi-step algorithms, progress also requires inspectable intermediate
outputs:

```text
stage -> artifact -> pass/fail criteria -> representative examples -> next-stage handoff
```

Do not debug only the final output of a pipeline. Each stage must expose enough
evidence to explain why examples pass, fail, or become uncertain before the next
stage consumes them.

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

### 6. Measure And Look

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

### 7. Instrument Multi-Step Algorithms

When the algorithm has multiple stages, treat each stage as a falsifiable
sub-task. Before trusting the full pipeline, create stage-local diagnostics.

For each stage, record:

```text
input count and distribution
accepted output count and distribution
rejected output count by reason
intermediate artifacts saved to disk
representative pass examples
representative fail examples
handoff contract to the next stage
```

For frame/sequence/spatial algorithms, include per-frame or per-region debug
views, not just aggregate metrics.

Example:

```text
candidate features -> matched tracklets -> triangulated points -> merged anchors -> surface regions
```

Each arrow must have debug evidence. If final anchors fail, inspect candidate
selection, matching, triangulation, merge, and promotion separately before
changing the model.

### 8. Diagnose Failures Before Adding Complexity

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

### 9. Record The Research State

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
