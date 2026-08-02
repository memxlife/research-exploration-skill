# Learned-Model Annex

Use this annex only when an active stage fits a parameterized representation,
dynamics model, estimator, or policy from data. It extends the base Mathematical
Model contract; it does not apply to inactive questions or fixed diagnostics.

## Completion Contract

### Variables and state

Separate observed inputs, latent or inferred variables, learned parameters,
outputs, and state passed forward. Do not call evaluation truth an observed
model input.

### Trainable objective

State the exact constrained objective, likelihood, or posterior. Define every
optimized variable, term, coefficient, aggregation, unit, and normalization
that affects the trade-off. Name the physical prior or coupled prior set each
term realizes.

Desired-property equations and evaluation residuals are not a training
objective.

### Admissible state and constraints

State the allowed state space and hard constraints, such as group membership,
proper rotation, positive depth, probability normalization, causal cutoff, or
feasible action. Say how computation enforces each one: parameterization,
projection, constrained solve, or rejection.

### Shortcut and degeneracy audit

Check every relevant shortcut:

```text
constant or collapsed representation
label, identity, or target copying
appearance-to-target memorization
scale, gauge, reflection, or coordinate ambiguity
future-observation or held-out leakage
privileged pose, trajectory, correspondence, mask, depth, or identity
one objective term dominating because units or counts differ
```

For each relevant shortcut, name the objective term, constraint, data boundary,
diagnostic, or claim restriction that excludes it. If no lawful exclusion is
known, mark the model incomplete.

### Supervision and no-leakage boundary

Declare separate schemas for:

```text
operational/deployment inputs
permitted training supervision and its provenance
development information used for checkpoint or operating-point selection
evaluation-only confirmation truth
```

The learner, pseudo-label generator, checkpoint selector, candidate generator,
matcher, fitter, and per-example decision must reject evaluation-only fields.
Any access is a protocol failure, even if it improves the metric.

### Training versus evidence

Mark each quantity as:

- `TRAIN`: contributes gradients or fitting;
- `DEVELOPMENT`: selects a checkpoint or operating point; or
- `CONFIRMATION`: untouched until the model and decision rule are frozen.

The same example or label cannot both fit and independently confirm the same
claim.

### Objective-to-computation map

For each objective term and hard constraint, record:

| Mathematical item | Prior | Permitted data | Computation | Training signal/artifact | Separate confirmation evidence |
|---|---|---|---|---|---|

No term may exist only in prose, and no training loss may appear in computation
without a named mathematical and physical role.

## Result

- **PASS:** every clause above is explicit and mutually consistent.
- **FAIL:** optimized variables, objective, constraints, shortcut controls,
  supervision, split roles, or the objective-to-computation map are missing.
- **NOT APPLICABLE:** no active parameterized model is being fitted.

Do not code or train while this annex is `FAIL`.

## Forward Checks

```text
FAIL: A document says corresponding features should be invariant and held-out
      residuals will test them, but it gives no trainable objective,
      anti-collapse term, lawful supervision, or train/confirmation boundary.

PASS: The document identifies theta, the exact loss and constraints, raw
      training inputs, forbidden privileged fields, checkpoint data, untouched
      confirmation truth, collapse controls, and the code path for every term.

NOT APPLICABLE: A fixed geometry diagnostic has no learned parameters. It must
      still pass the base Mathematical Model and implementation contracts.
```
