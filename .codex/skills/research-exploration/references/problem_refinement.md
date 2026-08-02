# Research-Question Refinement

Use this reference to refine a question only when reasoning or evidence reveals
a smaller uncertainty, dependency, coupling, or boundary.

## Stable Problem Definition

For each active node, Problem Definition owns:

```text
current research question
importance and stable scope
parent/root question and upward-answer obligation
already revealed child questions and typed relations
```

Changing results, claim boundaries, current status, blockers, and the next test
belong in `Experiments and Iterative Evidence`, not in Problem Definition.

A research question may name a target capability such as recovering a
transformation or constructing invariant features. It must not silently select
an architecture, solver, loss, dataset, or numerical threshold.

## When To Refine

Create or revise a child only when:

- the parent contains separable causal questions;
- several assumptions prevent one experiment from being interpreted;
- a pipeline failure cannot be localized;
- an exception or boundary needs its own investigation;
- two questions are coupled and cannot yet be concluded independently; or
- a bounded answer exposes the next question required by the parent.

Do not generate a large tree in advance. Keep inactive children as questions
and relations only; do not pre-fill their priors, equations, algorithms, or
experiments.

For each new child, record:

```text
child research question
why its answer changes the parent
bounded answer it must return upward
refinement, dependency, and coupling relations
reasoning or evidence that caused activation
```

## Relations And Coupling

Use stable IDs when the program needs them. Distinguish:

```text
refines: opens one part of a broader question
depends-on: another answer is needed for interpretation
coupled-with: current evidence cannot identify the answers independently
```

For a materially coupled set, record one joint prediction, mathematical model,
experiment/evidence path, per-member answer obligation, identifiability limit,
and evidence that would permit separation. Do not pretend joint evidence
isolates one prior.

## Prior Relations

Record relations only when they change interpretation:

```text
independent: testable separately
dependent: one assumes another
coupled: only a joint consequence is identifiable
competing: predict different explanations for the same observation
```

Each active child must name the root priors it inherits or refines. A child
prior cannot be disconnected from the parent without an explicit reason.

## Proportional Artifacts

Keep one design for one active question. Add a child directory only when that
child becomes active. Add a research map only when multiple retained nodes make
graph navigation necessary. The map owns graph edges and the program frontier;
the node design owns its local theory; `Experiments and Iterative Evidence`
owns its current result and next decision.

Add experiment, result/viewer, iteration, or final-report artifacts only when
the corresponding stage exists. Never create empty placeholders or duplicate
editable bounded answers.

## Evidence Propagation

After an experiment, update in this order:

```text
direct result
-> measurement validity
-> affected implementation, model, prior, or question layer
-> bounded answer and claim boundary
-> affected relations and upward answer
-> next active question or blocker
```

Classify the result before changing the mechanism:

1. invalid measurement or experiment;
2. implementation failure;
3. mathematical-model failure;
4. physical-prior failure or boundary violation;
5. research-question failure; or
6. insufficient evidence.

A failed implementation does not automatically falsify the prior. A failed
proxy does not falsify the broader prior unless the evidence rules out the
other lawful operationalizations.

## Forward Checks

```text
FAIL: An inactive child is created with a network, loss, dataset, thresholds,
      and experiment before any reasoning or evidence activates it.

PASS: The parent records the child question and dependency only; its own design
      is created after evidence makes it active.

FAIL: Problem Definition contains changing run status and the next experiment.

PASS: Stable question/decomposition remain in Section 1; current evidence and
      next test remain in Experiments and Iterative Evidence.
```
