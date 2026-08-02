# Run-Ready Algorithm And Experiment Contract

Use this reference after the design's Computational Implementation passes. It
owns exact execution details; it does not repeat the scientific rationale
already stated in the design.

## Freeze The Run

Before running, record:

```text
design version or source revision
input data and schema
permitted and forbidden fields
fixed configuration and declared sweeps
randomness, seed, and reproducibility setting
exact ordered procedure or callable interface
pass, fail, break, and insufficient-evidence outcomes
metrics and thresholds
expected intermediate outputs
artifact and receipt paths
command and runtime/resource requirements
```

Every configuration value that changes scientific interpretation must already
be justified and frozen in the design. The experiment contract records its
exact executable value. Ordinary control-plane details—paths, commands, hashes,
GPU allocation, environment, and receipts—live here rather than in Section 5.

## Stage Contract

For each nontrivial run stage, state:

```text
input assumptions
exact operation
expected output
pass/fail/insufficient-evidence condition
named failure reason
observable diagnostic artifact
next-stage handoff
```

Words such as “match,” “fit,” “stable,” “local,” or “valid” are incomplete
until the exact computation or test is named.

## No-Leakage Check

Verify that the learner, pseudo-label generator, checkpoint selector,
candidate generator, matcher, fitter, threshold tuner, and operational path
cannot open confirmation-only fields. A confirmation result cannot select the
model or operating point for the same claim.

## Before Launch

A reader must be able to answer:

```text
What enters and what is forbidden?
What exact operation runs at each stage?
Which frozen design item does it realize?
What makes each stage pass, fail, break, or return insufficient evidence?
Where are intermediate and final artifacts saved?
Can any fitting or selection path access confirmation truth?
```

Do not run while any answer requires inventing a scientific or execution
choice.
