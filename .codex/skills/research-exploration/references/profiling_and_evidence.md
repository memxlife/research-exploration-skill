# Profiling And Evidence

## Contents

1. Use profiling to explain results
2. Record the minimum experiment report
3. Match comparisons before attributing a cause
4. Preserve fast turnaround
5. Compare against strong evidence
6. Instrument multi-step pipelines

Use this reference when planning, running, or reviewing experiments.

## Why Profiling Exists

Do not stop at a yes/no answer. The "why" comes from stage-level profiling.
Break the task into priors, models, computation stages, evidence at each stage,
and the failure interpretation for each stage.

For each stage, record:

```text
question: what is this stage supposed to prove or falsify?
input evidence: what entered the stage?
output evidence: what was accepted, rejected, or uncertain?
failure evidence: what failed and by which reason?
artifact: what file, plot, table, screenshot, or viewer state lets a human inspect it?
interpretation: what does this stage imply for the conjecture?
```

The final yes/no answer must be backed by:

```text
final result -> stage evidence -> bottleneck or support -> conjecture update
```

## Minimum Experiment Report

Every experiment needs direct measurements and evidence appropriate to the
claim:

```text
purpose
setup
parameters
metrics
representative good and bad cases when they help interpretation
visual evidence when the phenomenon is visual, spatial, or temporal
interpretation
next experiment
```

For spatial, temporal, or visual work, include visual examples when they expose
failure or structure that aggregate metrics hide. Do not create a viewer when
text, a table, or a small saved artifact communicates the evidence more clearly.

## Matched Comparisons Before Causal Attribution

A difference between two experiments does not identify its cause when the
experiments also change parameter shape, data geometry, normalization, or the
number of independent random terms. Before attributing a result to a loss,
architecture, mechanism, or dimension, write down the following for each side:

```text
exact vectors, predictions, decisions, or losses being compared
exact update, perturbation, or noise formula
parameter and state shapes
input and output dimensions
normalization and aggregation used by every reported metric
gradient or perturbation geometry
number and dependence of random terms
starting input-output behavior
data, example order, schedules, seeds, and paired randomness
assumptions required by each approximation or scaling claim
```

Keep method-to-method measurements separate from target-based measurements.
For example, a direct prediction difference asks whether two methods agree
with each other, while task loss asks whether either method agrees with the
target. One cannot substitute for the other without an explicit derivation.

Derive each prediction from its own equations. A shared symbol such as
dimension $d$ does not justify copying an exponent or concentration claim from
one model to another. State how normalization and averaging change the measured
exponent simply because of the calculation; otherwise a reporting convention
can be mistaken for a scientific improvement.

If the audit finds more than one relevant difference, use the smallest matched
control that keeps the starting observable behavior, data, evaluation metric,
and random-update procedure fixed while changing only the proposed cause. Pair
random draws when that pairing is mathematically meaningful. When efficient
sampling replaces explicit random choices, verify the equivalence on a small
explicit case before the full run.

Interpret the matched result using four outcomes:

```text
support: the predicted distinction appears and every required assumption check passes
refine: the mechanism appears, but the measured law or range differs
falsify: the matched evidence contradicts the prediction while assumptions hold
inconclusive: a required baseline, approximation, pairing, or numerical check fails
```

Do not turn an inconclusive assumption check into support or falsification. If
a matched control is impossible, state that the comparison cannot isolate one
cause and limit the claim to the observed association.

## Fast Turnaround

For slow research loops, make a fast micro-test first:

```text
known good examples
known bad examples
small number of observations, samples, or cases
stage-local artifacts
one or two parameter settings
clear stop condition
```

Full sweeps are useful only after the fast test shows the operationalization is
worth scaling.

Use known examples when possible:

```text
known good cases
known bad cases
known confusing cases
the observations, samples, or records most likely to explain the failure
```

Fast turnaround is part of the method. A slow full run is not a substitute for a
small test that teaches why the algorithm works or fails.

## Compare Against Strong Evidence

When a trusted reference, oracle, manual label, or controlled benchmark exists,
use it to understand the difference between true cases and false cases. Do not
only use it to compute one final score.

Ask:

```text
How do true positive cases look at the stage level?
How do false positive cases look at the stage level?
How do false negative cases look at the stage level?
Which measured variables separate them?
Which measured variables do not separate them?
```

## Multi-Step Pipelines

For a pipeline such as:

```text
candidate generation -> matching -> estimation -> merging -> final prediction
```

each arrow must have debug evidence. If the final prediction fails, inspect the
intermediate stages before changing the model.

Runtime evidence should include:

```text
input count and distribution
accepted output count and distribution
rejected output count by reason
intermediate artifacts saved to disk
representative pass examples
representative fail examples
```
