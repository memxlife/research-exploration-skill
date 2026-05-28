# Research Loop Checklist

Use this checklist when planning or reviewing a research experiment.

## Claim

- Is the claim one sentence?
- Is it falsifiable?
- Does it name the assumed prior?
- Does it avoid claiming more than the test can show?

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
- Does each sub-problem have its own falsification test?
- Are negative answers recorded as evidence, not discarded?
- Did the decomposition continue until the bottleneck became local and fixable?
- Is the final causal path stated from big failure to verified bottleneck?
- Were algorithm changes delayed until the failed sub-problem was identified?

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
- What changed in the hypothesis?
- What is the next smallest test?
