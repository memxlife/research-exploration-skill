# Research Documentation

Use this reference when writing or revising a research document.

## Two Documents

Separate the current theory from the research history:

```text
current-state document:
  the latest clean problem definition, priors, model, implementation contract,
  falsification plan, claim boundary, and current uncertainty

iteration ledger:
  the append-only sequence of conjecture -> operationalization -> profiling ->
  result -> interpretation -> goal audit when needed -> conjecture update
```

The current-state document should be rewritten as understanding improves. The
iteration ledger should preserve how that understanding changed.

Do not bury failed operationalizations inside the current model. Keep them in
the ledger as evidence about what was falsified and why.

## Testable Argument

When a research problem becomes more than a quick experiment, write it as:

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

Use this subsection format when helpful:

```text
Objective: what this part tries to do
Physical prior: why this step is plausible in the world
Model: the equation or formal representation
Implementation contract: the code stage, inputs, outputs, and pass/fail checks
Evidence: metrics, visual examples, and failure cases
```

## Iteration Record

For each iteration, record:

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

When the goal changes, record:

```text
Old goal: what the work was trying to optimize.
Why it failed: what repeated profiling showed.
Downstream purpose: what the result is actually used for.
New goal: what should be optimized now.
Metric change: how success and failure are measured now.
Accepted errors: which old errors are now acceptable or useful.
Rejected errors: which errors remain harmful.
```

## Equation And Parameter Rules

Every equation must map to:

```text
physical prior
model variable
implementation stage
experiment or profiling artifact
```

Every hyperparameter must have:

```text
name
value
definition
reason for this value
effect if too low or too high, when useful
```

Write simply. Rigor means precise, not fancy.
