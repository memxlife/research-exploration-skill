# Profiling And Evidence

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

Every experiment needs both numbers and visual evidence:

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

For spatial, temporal, or visual work, include visual examples whenever
possible. Aggregate metrics alone are not enough.

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
