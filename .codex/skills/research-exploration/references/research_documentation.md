# Research Documentation

Use this reference when writing or revising a research document.

## Contents

1. Separate current state from history
2. Write the four-part testable argument
3. Maintain the program research map
4. Record each iteration
5. Map equations and parameters to evidence

## Current State And History

For each active node, separate current theory from research history:

```text
<node-dir>/design.md:
  the latest clean research question, physical priors, predicted consequences,
  model, implementation contract, claim boundary, and bounded answer

<node-dir>/iterations.md:
  the append-only sequence of research question -> conjecture ->
  operationalization -> falsification and profiling -> result ->
  interpretation -> question or conjecture update
```

The current-state document should be rewritten as understanding improves. The
iteration ledger should preserve how that understanding changed.

Do not bury failed operationalizations inside the current model. Keep them in
the ledger as evidence about what was falsified and why.

## Testable Argument

When a research problem becomes more than a quick experiment, write it as:

```text
1. Problem Definition
   current research question
   importance and scope
   parent question and required upward answer
   child research questions and typed relations
   current bounded answer and claim boundary
   local frontier or answered/blocked state
2. Physical Priors
   conjectured structure and predicted observable consequences
   relations among independent, dependent, coupled, or competing priors
3. Mathematical Model
4. Computational Implementation
   falsification and stage-level profiling support
```

Use this subsection format inside the four-part design when helpful:

```text
Objective: what this part tries to do
Physical prior: why this step is plausible in the world
Model: the equation or formal representation
Implementation contract: the code stage, inputs, outputs, and pass/fail checks
Evidence: metrics, visual examples, and failure cases
```

When a child question reaches the active frontier, make it the current question
of a new four-part research unit. Keep inactive children as research questions
and relations only; do not pre-fill their priors, equations, or implementations.

Do not force a research question into an input-output benchmark specification
at the inspiration stage. A question may name the capability or object being
sought. Add operational variables, thresholds, and pass conditions when forming
the conjecture and experiment. Keep any dataset or numeric threshold supplied
by the operationalization out of the broader question unless the researcher
defined it there.

## Research Map

Once the work contains multiple retained research questions, maintain:

```text
docs/research_map.md

node ID and research question
parent and upward-answer contract
refinement source: researcher, causal reasoning, or evidence artifact
refinement, dependency, and coupling edges
status and document path, or none (not yet materialized)
pointer to the authoritative bounded answer, or none (unanswered/unmaterialized)
program active frontier
coupled-set contracts and shared evidence paths
```

Use stable per-node directories under `docs/problems/<ID>/` for newly active
questions. Existing root documents may remain mapped to `P0`; do not duplicate
research records only to normalize paths. The map is authoritative for graph
relations, coupled-set contracts, and the program frontier. Node documents own
their local current state and history. Do not maintain a second editable copy
of a node's bounded answer in the map. Keep an inactive child's question in its
parent design and do not create its node directory until activation.

## Iteration Record

For each iteration, record:

```text
Research question: what is being answered in this iteration.
Physical-structure conjecture: what regularity is believed and under what scope.
Predicted consequence: what should be observed if the conjecture is correct.
Physical parameterization: which measurable version of the idea is being tested.
Operationalization: how the parameterization becomes variables, thresholds, or stages.
Profiling plan: what intermediate evidence will explain success or failure.
Result: metrics, artifacts, and representative examples.
Interpretation: what succeeded, what failed, and why.
Question or conjecture update: what changes in the current-state document.
Next uncertainty: the smallest remaining uncertainty to isolate.
Hierarchy update: what changes in the current node, related nodes and priors,
the upward answer, and the active frontier.
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
