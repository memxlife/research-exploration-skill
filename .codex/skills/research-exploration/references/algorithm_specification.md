# Algorithm Specification

## Contents

1. Reject hand-waved algorithms
2. Record the required specification
3. Align physical, mathematical, and computational layers
4. Map active learnable objectives into code
5. Define stage contracts and algorithm blocks
6. Complete the pre-run check

Use this reference when the research task contains a nontrivial algorithm.

## No Hand-Waving

Do not run an experiment until the algorithm is written in exact, simple words.
Words like "cluster," "match," "stable," "local," "valid," or "consistent"
are not enough by themselves. Define the exact test.

## Required Specification

For each nontrivial algorithm, write:

```text
input
parameters
intermediate variables
step-by-step procedure
pass conditions
fail conditions
failure reasons
outputs
debug artifacts
```

Every parameter must have:

```text
name
value
meaning
why this value is used
expected effect if too small
expected effect if too large
```

## Align The Layers

Before coding or running a benchmark, check the alignment:

```text
physical prior:
  what should happen in the world?
math model:
  what variables measure that thing?
algorithm:
  what exact steps compute those variables?
experiment:
  what result would support or falsify the model?
```

If the implementation has a heuristic that is not in the prior or math, either
remove it or explicitly name it as an implementation heuristic.

Before choosing one implementation, list the possible measurable versions of the
prior. If a key idea can mean more than one thing, name the alternatives in
plain words. Do not silently choose one and treat it as the whole prior.

When evidence unfolds over time or changing conditions, distinguish:

```text
single-observation evidence: what is true in one observation
change evidence: what persists or changes across observations
summary evidence: what is true after combining observations
```

Do not replace change evidence or summary evidence with a single-observation
proxy unless that simplification is the test.

## Learnable Objective To Code

When the active stage has selected a learnable model, do not implement or train
it until the Learnable-Model Completion Gate in
[learnable_model_completion.md](learnable_model_completion.md) passes. For every
objective term and hard constraint, specify:

```text
mathematical name and physical prior
permitted input fields and split
exact function or module that computes it
aggregation, units, normalization, and coefficient
constraint enforcement or rejection path
logged training artifact
separate profiling or held-out falsification artifact
```

The learner, objective, checkpoint selector, and threshold tuner must be unable
to read evaluation-only fields. A held-out result cannot also select the model
for the same claimed test. If code contains a loss or regularizer absent from
the mathematical model, stop and add its physical role or mark it as an
implementation heuristic before running.

## Stage Contract

For each stage in a multi-step algorithm, write:

```text
input assumptions
sub-task objective
exact algorithm steps
expected intermediate output
pass/fail criterion
named failure reasons
debug artifact
representative pass examples
representative fail examples
next-stage handoff contract
```

After the stage runs, record:

```text
input count and distribution
accepted output count and distribution
rejected output count by reason
intermediate artifacts saved to disk
```

## Algorithm Block

For algorithm-heavy documents, use this format:

```text
Algorithm:
1. Read these inputs.
2. Compute these intermediate variables.
3. Apply this decision rule.
4. If the rule fails, record this failure reason.
5. Save these outputs and debug artifacts.
```

The algorithm is part of the research claim. If the algorithm is vague, the
experiment cannot falsify the conjecture because nobody knows what was tested.

## Before Running

Before running the algorithm, make sure a reader can answer:

```text
What exact data enters the algorithm?
What exact data is ignored?
If the model learns, which objective term does each training computation realize?
How is each hard constraint enforced?
Which shortcut or collapse does each exclusion prevent?
Can any training or selection code access evaluation-only fields?
What does each step compute?
What can make the step say yes?
What can make the step say no?
What can make the step say insufficient evidence?
Where can a human inspect the intermediate result?
```
