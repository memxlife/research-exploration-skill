# Recursive Research-Question Refinement

Use this reference to manage coarse-to-fine research without losing the causal
relationship between the motivating question and the experiment being run.

## Contents

1. Center each unit on a research question
2. Separate questions from mechanisms
3. Follow the four-part research loop
4. Refine only when exploration reveals a reason
5. Represent relations and the active frontier
6. Model relations among physical priors
7. Preserve the hierarchy on disk
8. Propagate evidence through the graph
9. Physical-AI example

## Center each unit on a research question

For every active research unit, write `Problem Definition` in this order:

```text
1. Current research question
   The open question being answered now.

2. Importance and scope
   Why the answer matters, what decision it changes, and what is in scope.

3. Parent question and upward-answer contract
   The larger question that created this one and the bounded answer this unit
   must return.

4. Child research questions and relations
   Smaller questions already revealed by reasoning or evidence, with explicit
   refinement, dependency, and coupling relations.

5. Current bounded answer and claim boundary
   What is currently supported, including "unanswered" at the start.

6. Local frontier
   The smallest descendant question or coupled set suggested by this node.
```

A root uses `parent: none (root)`. A current leaf may use
`children: none (current leaf)`. An answered node may use
`local frontier: none (answered)`. A blocked node names the missing evidence
or dependency rather than inventing a next step.

## Separate questions from mechanisms

A research question may explicitly name the object or capability being sought:

```text
How can distinguishable visual features be captured across observations?
How can those features be physically grounded?
How can a shared spatial transformation be extracted?
How can transformation-invariant visual features be generated?
How can this structure improve data efficiency?
```

These remain research questions. They do not become mechanisms until a solver,
architecture, loss, representation, or algorithm is selected. Do not weaken a
clear research question into vague language merely because it names a
transformation, feature, representation, or capability.

At the inspiration stage, do not force every question into a closed benchmark
specification. State enough scope to know what is being sought. Add precise
variables, thresholds, and pass conditions when deriving a falsifiable
conjecture and experiment. Do not insert a dataset, numeric target, or solution
assumption into the research question unless the researcher supplied it. When
qualitative language needs an experimental threshold, label and justify that
operational choice without rewriting the broader question.

## Follow the four-part research loop

Every active question uses:

```text
1. Problem Definition
2. Physical Priors
3. Mathematical Model
4. Computational Implementation
```

Problem refinement is not a fifth section. It is a feedback operation that may
create or reconnect four-part research units after reasoning or evidence changes
the question graph.

Apply the loop as:

```text
research question
  -> conjecture about physical structure
  -> predicted observable consequence
  -> mathematical model
  -> computational implementation
  -> falsification and profiling
  -> improved understanding of the structure
  -> refined question or conjecture
```

The physical prior is the structural core of the conjecture. The full
falsifiable conjecture combines that prior with a predicted observation and
the conditions under which the prediction should hold.

Computational implementation is not only construction of a proposed solution.
It must make falsification and profiling possible. Expose intermediate
artifacts that reveal whether the question framing, prior, model, algorithm,
data, or measurement explains the result.

## Refine only when exploration reveals a reason

Do not generate a large problem tree at the beginning. Create or revise child
questions when reasoning, falsification, or profiling reveals that:

- the current question contains separable causal questions;
- several assumptions prevent one experiment from being interpreted;
- a pipeline failure cannot be localized without a smaller question;
- an exception or boundary condition requires its own investigation;
- two questions or priors are coupled and must be studied together; or
- a bounded answer exposes the next question required by the parent.

When a child becomes active, make it the current research question of a new
four-part unit. Initially record inactive children as questions and relations
only. Do not pre-fill their priors, equations, algorithms, or experiments.

For each proposed child, record:

```text
child research question:
why answering it changes the parent answer:
answer returned to the parent:
known relations to other questions:
evidence or reasoning that caused this refinement:
```

## Represent relations and the active frontier

Use stable identifiers such as `P0`, `P0.1`, and `P0.2`. Keep different edge
types explicit:

```text
refines:      the child opens one part of a broader question
depends-on:   one answer is needed to interpret another
coupled-with: the questions cannot currently be concluded independently
```

Do not force these relations into a strict tree. Refinement, dependency, and
coupling form a graph.

The active frontier is usually one question. When questions cannot be tested or
interpreted independently, use the smallest coupled set required. The frontier
may also use oracle inputs to test a downstream conjecture early; record the
oracle assumption and do not treat that result as end-to-end evidence.

For every coupled question or prior set, create a first-class joint contract:

```text
coupled-set ID:
member question and prior IDs:
why the members are not currently identifiable independently:
joint predicted consequence and falsifier:
joint mathematical model:
shared experiment and result path:
answer obligation for each member:
pointer to each member's authoritative bounded answer:
joint-identifiability limitation shared by the members:
evidence that would allow the set to be decoupled:
```

Each member keeps its own research-question unit, but links to the shared
contract instead of duplicating or pretending to isolate joint evidence.

## Model relations among physical priors

Give important priors stable IDs such as `PR1` and record:

```text
conjectured physical structure:
scope and boundary conditions:
predicted observable consequence:
possible falsifier:
relation to other priors:
mathematical model or models that represent it:
```

Classify prior relations when they matter:

```text
independent: can be tested and modeled separately
dependent: one prior assumes another
coupled: only their joint consequence is currently identifiable
competing: they predict different explanations for the same observation
```

A mathematical model may realize one prior or a coupled set. Do not claim that
one prior was isolated when the experiment only tested their joint consequence.

## Preserve the hierarchy on disk

For one research question, the three working documents may remain directly in
`docs/`. Once refinement creates multiple retained questions, add:

```text
docs/research_map.md
docs/problems/<ID>/design.md
docs/problems/<ID>/experiment_design.md
docs/problems/<ID>/visualization_results.md
docs/problems/<ID>/iterations.md
```

Map existing root documents to `P0` rather than duplicating them only to change
layout. In `docs/research_map.md`, record:

```text
node ID and research question
parent and upward-answer contract
refinement source: researcher, causal reasoning, or evidence artifact
refinement, dependency, and coupling edges
status: unexplored, active, blocked, answered, or retired
document path, or none (not materialized; question lives in parent design)
pointer to the authoritative bounded answer, or none (unanswered/unmaterialized)
program active frontier
coupled-set contracts and shared evidence paths
```

`docs/research_map.md` is authoritative for graph edges, coupled-set contracts,
and the program active frontier. Each node's `design.md` owns its local question,
priors, models, bounded answer, and local frontier. Each node's `iterations.md`
is the append-only history for that node. Existing root documents mapped to
`P0` use `docs/iterations.md`. Do not duplicate editable bounded-answer prose
in the map. Do not create a child directory until that question becomes active.

## Propagate evidence through the graph

After every experiment, update in this order:

```text
direct evidence
  -> validity of the test and measurement
  -> affected research layer
  -> current bounded answer and claim boundary
  -> affected question and prior relations
  -> answer returned to ancestors
  -> active frontier
```

Classify what the evidence changes before modifying the mechanism:

1. **Invalid experiment or measurement:** the test cannot support the intended
   comparison.
2. **Computational-implementation update:** the model may be adequate, but the
   algorithm, code, data path, or numerical method did not realize it.
3. **Mathematical-model update:** the prior may hold, but the model did not
   express, identify, or preserve the required structure.
4. **Physical-prior update:** the conjectured structure was absent, incomplete,
   coupled to another prior, or outside its stated scope.
5. **Research-question update:** the importance, scope, objects, or causal
   decomposition of the question must change.
6. **Insufficient evidence:** the test did not distinguish these alternatives.

Propagate evidence sideways or downward when siblings, descendants, or shared
priors depend on the changed claim. A failed implementation must not
automatically falsify its mathematical model or physical prior.

## Physical-AI example

Assume the researcher supplied the following initial questions during
inspiration. Record them as a provisional map, not as an exhaustive tree.

```text
P0 Current research question:
  How can a physical agent learn physically grounded, viewpoint-consistent
  visual representations with substantially less training data?

P0 child research questions:
  P0.1 How can distinguishable visual features be captured across observations?
  P0.2 How can distinguishable features be grounded in persistent 3D entities?
  P0.3 How can shared spatial transformations be extracted from sparse grounded
       features?
  P0.4 How can invariant or equivariant visual features be generated from the
       recovered transformations?
  P0.5 How can the resulting structure improve measured data efficiency?

Relations:
  P0.2 depends partly on P0.1;
  end-to-end P0.3 depends on P0.2;
  P0.4 depends on what P0.3 can recover;
  P0.5 depends on the joint pipeline and must not hide supervision costs.

Refinement source:
  researcher-provided initial questions plus the dependency reasoning above;
  no grandchildren are created until falsification or profiling reveals them.
```

If the immediate decision is whether the shared-transformation prior is worth
pursuing, activate `P0.3` with oracle grounded correspondences for a fast
upper-bound test. If the immediate uncertainty is whether stable physical
identities exist, activate the coupled frontier `{P0.1, P0.2}`. In either case,
the active node starts with its research question, not a preferred network,
solver, or optimizer.
