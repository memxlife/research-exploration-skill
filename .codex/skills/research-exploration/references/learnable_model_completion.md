# Learnable-Model Completion

Use this reference when an active research stage selects, specifies, or reviews
a parameterized representation, dynamics model, estimator, or policy that will
be learned.

## Contents

1. Decide whether the gate applies
2. Complete the mathematical model
3. Declare fixed non-learning baselines
4. Review the gate result
5. Run the compact forward test

## Trigger

Apply the gate only after both conditions hold:

1. the research stage is active; and
2. the stage has selected a parameterized model whose parameters or latent
   state will be fitted from data.

Do not apply it to an inactive child question, an open physical conjecture, or
a fixed diagnostic computation. Do not use the gate to insert a loss,
architecture, solver, dataset, or threshold into the broad research question.
It formalizes a learnable model only after that model has been selected at the
active stage.

## Completion Contract

The Mathematical Model is incomplete until a reader can recover all eight
parts below without inventing missing facts.

### 1. Variables and state

State separately:

```text
observed inputs available to the learner
latent or inferred variables
learned parameters
model outputs and state passed forward
```

Do not call an evaluation reference an observed model input. Keep deployment,
training-supervision, and evaluation-only quantities distinct.

### 2. Physical-prior mapping

For every term or constraint, name the physical prior or coupled prior set it
realizes and the observable consequence it is intended to produce. A generic
regularizer without a structural role is an implementation choice, not a
physical-prior term.

### 3. Constrained objective

Write the exact optimization target, or an explicitly declared likelihood or
posterior objective. Identify the optimization variables and every term. For
example, use the relevant form rather than copying this template blindly:

$$
\min_{\theta,\,z}
\sum_k \lambda_k\,\mathcal L_k(\theta,z;D_{\mathrm{train}})
\quad\text{subject to}\quad
(\theta,z)\in\mathcal A.
$$

Define each term, coefficient, unit, scale, aggregation, and normalization
when these affect the tradeoff. If the model uses a likelihood or posterior,
state the random variables, conditioning information, factorization, and
assumptions instead of disguising it as an unnamed loss.

### 4. Admissible state and hard constraints

State the allowed state space and hard constraints, such as a proper rotation,
group membership, positive depth, probability normalization, causal cutoff,
feasible geometry, or policy action set. State how the later computation
enforces each constraint: parameterization, projection, constrained solve, or
explicit rejection.

### 5. Degeneracy and shortcut exclusions

List every known solution that can minimize the objective without realizing
the intended prior. At minimum check for:

```text
constant or collapsed representation
identity or label copying
memorized appearance-to-target lookup
scale, gauge, reflection, or coordinate ambiguity
future-observation or held-out leakage
privileged pose, trajectory, correspondence, mask, depth, or identity use
one term dominating because units or counts differ
```

For each relevant shortcut, name the term, constraint, data split, controlled
diagnostic, or claim restriction intended to exclude it. If no exclusion is
known, record the model as incomplete rather than assuming the shortcut away.

### 6. Supervision and no-leakage schema

Declare the exact permitted training fields and their provenance. Declare every
forbidden or privileged field. Use separate schemas or physically separate
artifacts for:

```text
operational/deployment inputs
permitted training supervision
evaluation-only references
```

The learner, objective, checkpoint selector, threshold tuner, and operational
pipeline must reject evaluation-only fields. Any access is a protocol failure,
even when it improves the metric.

### 7. Training versus falsification evidence

Mark every mathematical term as one of:

```text
TRAIN: contributes gradients, fitting, model selection, or threshold selection
DIAGNOSTIC: inspected during development but does not fit the selected model
HELD-OUT: untouched until the model, checkpoint, and criteria are frozen
```

Held-out transform prediction, physical interaction, or another falsification
metric cannot also be a training term for the same claimed test. If a quantity
serves both roles on different data, name the disjoint splits explicitly.

### 8. Objective-to-computation map

Provide one row per objective term and hard constraint:

| Mathematical item | Prior realized | Permitted data | Code path | Training artifact | Profiling or falsification artifact |
|---|---|---|---|---|---|
| named term or constraint | named prior | exact schema/split | function or stage | logged contribution/state | residual, example, or held-out result |

No term may exist only in prose, and no training loss may appear in code without
a named mathematical and physical role.

## Fixed Non-Learning Baseline

An active fixed diagnostic baseline may deliberately have no learnable
objective. Its Mathematical Model must say:

```text
learnable objective: none
fixed mechanism being tested
why fixing it isolates the current physical or computational question
parameters that are set rather than learned
evidence the baseline can and cannot provide
which later selected learnable stage must pass this completion gate
```

This declaration does not exempt a learned successor.

## Gate Review

Return one explicit result:

- **PASS:** all eight parts are present and mutually consistent.
- **FAIL:** the active stage claims a learnable model but omits an objective,
  variables, constraints, shortcut exclusions, supervision boundary,
  train/held-out separation, or implementation mapping.
- **NOT APPLICABLE:** the stage is inactive/open, or it is a declared fixed
  non-learning baseline with the required explanation.

Do not code or train an active learnable model while the result is `FAIL`.

## Compact Forward Test

Use this review fixture after revising the skill:

```text
Candidate document: an active stage says it will learn a representation
h_theta. It gives equations saying same-object features should be invariant,
spatial state should transform predictably, and held-out residuals will test
both properties. It names a dataset and evaluation metrics, but it does not
define optimized variables, a constrained objective, anti-collapse terms,
permitted supervision, or the training/evaluation data boundary.
```

Expected result: **FAIL**. Equations describing desired behavior and evaluation
tests do not specify what training computes.

False-positive guard: an inactive research question must not be forced to pick
an objective, and a declared fixed geometry baseline with the complete
no-learning statement must return **NOT APPLICABLE**, not `FAIL`.
