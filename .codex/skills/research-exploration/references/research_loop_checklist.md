# Research Loop Checklist

Use this checklist when planning or reviewing a research experiment.

## Contents

1. Check the question hierarchy, claim, and physical priors
2. Check the Learnable-Model Completion Gate when it applies
3. Check operational definitions and the benchmark
4. Check recursive decomposition and metrics
5. Check visualization and stage contracts
6. Check implementation and interpretation

## Problem Hierarchy

- Is the current research question stated before its parent and children?
- Is its importance, scope, and affected decision explicit?
- Is the parent question named with the bounded answer returned upward?
- Is every child phrased as a research question?
- Does each child name what must be understood or achieved without selecting a
  solver, architecture, loss, or algorithm?
- Does the question avoid invented datasets, solution assumptions, and numeric
  thresholds that belong to a later operationalization?
- Does every child record whether it came from the researcher, causal reasoning,
  or experimental evidence?
- Are refinement, dependency, and coupling edges distinguished?
- Is the active frontier the smallest question or coupled set needed now?
- Does every coupled set have one joint prediction, model, shared evidence path,
  per-member answer obligation and pointer, joint-identifiability limitation,
  and decoupling condition?
- Did the hierarchy emerge from reasoning or evidence instead of being
  exhaustively invented upfront?

## Claim

- Is the claim one sentence?
- Is it falsifiable?
- Does it name the conjectured physical structure?
- Does it state the observable consequence expected if that structure holds?
- Does it avoid claiming more than the test can show?

## Physical Priors

- Is each prior a structural claim about the world or workload?
- Are its scope and boundary conditions explicit?
- Are independent, dependent, coupled, and competing priors distinguished?
- Does each mathematical model name the prior or coupled set it represents?

## Learnable-Model Completion Gate

- Is the stage active, and has it selected a parameterized representation,
  dynamics model, estimator, or policy to learn? If not, do not force a loss.
- If it is learnable, are observed inputs, latent variables, learned parameters,
  and outputs/state explicit?
- Does every objective term realize a named physical prior or coupled prior set?
- Is the exact constrained objective, likelihood, or posterior objective stated,
  with term meanings, units, and normalizations where relevant?
- Are the admissible state space and hard geometry, group, causal, or action
  constraints explicit?
- Are collapse, memorization, gauge, reflection, future leakage, privileged-
  label, and term-scaling shortcuts named with their intended exclusions?
- Are permitted supervision and forbidden fields enforced by separate
  operational, training, and evaluation-only schemas?
- Are training terms distinct from untouched held-out falsification evidence?
- Does every objective term and constraint map to a code path, training
  artifact, and profiling or held-out artifact?
- If the active stage is a fixed baseline, does it explicitly state no
  learnable objective, the mechanism isolated, its claim boundary, and the
  later learned stage that must pass the gate?
- Would a document that claims to learn a representation but contains only
  desired-property equations and evaluation tests be rejected as incomplete?

## Operational Definitions

- Are key terms measurable?
- Are ambiguous and missing evidence separated?
- Is success defined before running the test?
- Is failure allowed to teach something specific?

## Benchmark

- Does the benchmark isolate one question?
- Is ground truth available for the exact thing being evaluated?
- Can a human visually inspect the setup?
- Does the setup contain enough variation to expose the prior?
- Are the important variations intentionally designed, not incidental?

## Recursive Decomposition

- Is the big failure decomposed into smaller possible failure points?
- Does each activated research question have its own falsification test?
- Does an active child become the current question of a recursive four-part unit?
- Were priors, equations, and implementations deferred until that child became active?
- Are negative answers recorded as evidence, not discarded?
- Did the decomposition continue until the bottleneck became local and fixable?
- Is the final causal path stated from big failure to verified bottleneck?
- Were algorithm changes delayed until the affected research layer or question
  was identified?

## Metrics

- Does each metric answer a specific question?
- Are thresholds and units stated?
- Are top-line metrics supported by examples?
- Are false positives and false negatives shown separately?
- Do false positives and false negatives have the same cost?
- Does the metric match the downstream purpose?

## Visualization

- Are good and bad cases shown?
- For spatial work, is there a 3D or frame-by-frame view?
- Can the viewer distinguish prediction, ground truth, and uncertainty?
- Are visual encodings chosen so the evidence is not confused with the raw data?

## Stage Contract

- Are input assumptions stated before implementing the sub-task?
- Is the sub-task objective narrow enough to falsify locally?
- Is the expected intermediate output defined before running the code?
- Is there a pass/fail criterion for the intermediate output?
- Is there a debug artifact that a human can inspect?
- Are representative success and failure cases named or saved?
- Is the next-stage handoff contract explicit?

## Implementation

- Are code paths listed?
- Are commands reproducible?
- Are hyperparameters documented with values and reasons?
- Are heuristics separated from priors?
- Are generated artifacts small enough to commit, or clearly ignored?

## Interpretation

- What is validated?
- What failed?
- What remains uncertain?
- What changed in the research question, prior, model, or implementation?
- Was the experiment valid, invalid, or insufficiently distinguishing?
- What bounded answer propagates to the parent question?
- Which related questions or shared priors are affected?
- How did the child questions, relations, or active frontier change?
- Were the authoritative research map and the node's append-only
  `iterations.md` updated?
- What is the next smallest test?
