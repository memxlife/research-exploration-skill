# Stage-Aware Research Audit

Use only the blocks that apply to the current stage. Any applicable missing
contract is `FAIL`; an inactive future stage is not required to choose a model,
loss, dataset, or threshold.

## Question And Document

- Is the current question stated before any mechanism?
- Are importance, scope, parent/root relation, and already revealed children
  clear without chat history?
- Is the four- or five-section structure declared and justified?
- Does each section contain only content it owns?
- Does every child inherit or explicitly refine named root priors?
- Were inactive variants, downstream work, duplicate warnings, and operational
  receipts removed or linked rather than copied?
- Can a cold reader summarize each major section in one sentence?
- Does Section 6 contain a rolling summary derived from its experiment rounds
  rather than an independent status narrative?
- If the child has a stable bounded conclusion, was the living design compacted
  to its summary, final claim boundary, decision-changing findings, and links
  while every complete round remains preserved exactly once in a final report
  or append-only evidence ledger?

## Physical Priors

- Is every prior a falsifiable external world/workload claim with an observable
  consequence and scope?
- Would it remain a world claim if no algorithm or experiment existed?
- Are candidate policies, thresholds, splits, leakage controls, held-out rules,
  and validation procedures absent?
- Are dependent, coupled, or competing priors named only where interpretation
  requires them?

## Mathematical Model

- Are observed, latent/inferred, decision/output variables, and admissible state
  defined as needed?
- Is the exact goal or constrained objective stated?
- Does each constraint or term arise from a named prior?
- Are permitted and forbidden information explicit?
- Are development operating-point selection and untouched confirmation claims
  distinct?
- Would a fixed matcher with equations but no precision-versus-coverage goal
  fail?

### Learned annex, when applicable

- Are trainable variables and the exact objective explicit?
- Are hard constraints and their enforcement stated?
- Are collapse, memorization, ambiguity, leakage, and relevant geometric
  shortcuts paired with exclusions or bounded claims?
- Are operational, training, development, and confirmation schemas separated?
- Can every objective term be traced to permitted data, computation, training
  evidence, and separate confirmation evidence?

## Prior Art, When Applicable

- Was the search driven by the current question, mathematical constraints, and
  supervision boundary?
- For every representative method, are Problem, How it works, Why, Strengths
  and limits, and the direct Decision explained in that order?
- Does `How` state the input, measured/constructed intermediate, and how the
  procedure produces its output?
- Does `Why` causally connect the motivating structure to the mechanism instead
  of merely naming a prior?
- Were hidden pose, depth, correspondence, mask, track, optical-flow, synthetic
  warp, reward, future-data, and pretraining teachers audited?
- Does Section 4 end in direct adopt/adapt/baseline/external-only/reject
  decisions that Section 5 implements?

## Computational Implementation

For an active learnable model, are these subsections present once and in order?

```text
5.1 purpose and input/output
5.2 prior-to-mechanism design pipeline using Goal / How / Why per stage
5.3 architecture and frozen design parameters
5.4 training computation
5.5 inference and decision computation
5.6 evaluation boundary and experiment-contract link
```

- Can an independent implementer reproduce the scientific computation without
  inventing a choice?
- Is every outcome-changing variable frozen, part of a frozen sweep, or marked
  `BLOCKED`?
- In Section 5.2, does every computational stage state:
  - **Goal:** the uncertainty or subproblem it resolves;
  - **How:** exact operation, tensors/state, and relevant parameters; and
  - **Why:** prior and mathematical bias, intended behavior, and important
    residual limitation?
- Does every significant mechanism trace to a prior and mathematical item, or
  carry an explicit engineering classification with no unsupported claim?
- Are accepted output, refusal, error, and break behavior explicit?
- Are commands, paths, hashes, resources, and receipts kept in the experiment
  contract?

A fixed non-learning design may use a documented reduced form, but it must
preserve input/output, causal mechanism map, exact algorithm, decision/refusal,
and evaluation boundary.

## Experiment And Evidence, When Applicable

- Is the smallest distinguishing test preregistered?
- Are schemas, splits, criteria, metrics, statuses, resources, and artifact
  paths frozen before execution?
- Is confirmation truth inaccessible to training, checkpoint selection,
  candidates, fitting, thresholds for the claimed confirmation, and per-example
  decisions?
- Is the direct result reported before document or viewer polish?
- Does stage-level evidence localize invalid measurement, implementation,
  mathematical-model, physical-prior, question, or insufficient-evidence
  outcomes?
- Is visual evidence included only when it helps inspect the claim?
- Does every round state Question, Setup/model and controlled variables,
  Training data, Testing/confirmation data and split, Results or `NOT RUN`, and
  Insight/claim update/next decision?
- Does a planned round explicitly say `NOT RUN`, and does a completed round
  link evidence for all six fields without fabricated results?
- Are commands, hashes, resources, and machine receipts linked externally while
  the main design retains the scientific setup/data/result/interpretation?

## Source And Viewer, When Applicable

- Did changed Markdown math pass `scripts/check_markdown_math.py`?
- If rendered math is in scope, was the exact target viewer probed and the final
  artifact inspected? Otherwise is rendering truthfully marked unverified?
- If a viewer exists, does every plot define data, metric, unit, axes, result,
  conclusion, and material uncertainty?

## Forward Regression Fixtures

```text
FAIL — mixed ownership:
  Problem Definition contains run status; Physical Priors contains split and
  leakage rules; Mathematical Model contains architecture and commands.

FAIL — no problem objective:
  A fixed descriptor ranks candidates but never states the precision/coverage
  trade-off used to choose strictness.

FAIL — incomplete learned model:
  A learned descriptor has invariance equations but no exact loss,
  anti-collapse control, lawful supervision, or confirmation boundary.

FAIL — hidden teacher:
  “Self-supervised” training obtains positives from pose, depth, optical flow,
      synthetic warps, or ground-truth correspondence forbidden by the design.

FAIL — shallow related work:
  “Shi--Tomasi scores two-dimensional gradient structure.” It does not explain
  how an image window and its gradients produce selected corners.

PASS — explanatory related work:
  An image window produces a local structure tensor from horizontal and
  vertical gradients; two strong eigenvalues select corners because their
  motion is constrained in both image directions, while an edge remains
  ambiguous along its length.

FAIL — generic computation:
  “A shared CNN produces unit descriptors, then matches them.”

FAIL — how-only pipeline:
  Section 5 gives exact operations and parameters, but no stage states what
  uncertainty it resolves or why the operation realizes a prior/objective.

FAIL — detached rationale:
  A global table mentions priors, while the pipeline stages themselves force
  the reader to cross-reference which rationale applies.

PASS — constructible causal stage:
  Goal: restrict correspondence uncertainty under bounded motion.
  How: mask B candidates outside the frozen 16-pixel window.
  Why: continuity implies bounded displacement, so the mask excludes physically
  implausible distant matches; fast motion can place the true match outside.

FAIL — evidence leakage:
  confirmation correspondence truth selects candidates, checkpoints,
  thresholds, or individual matches.

PASS — bounded evidence:
  raw-video training and validation freeze the model; development truth freezes
  acceptance strictness; untouched confirmation truth scores frozen decisions.

FAIL — results-only round:
  A metric table has no question, controlled setup, train/confirmation data, or
  interpretation.

FAIL — protocol-only round:
  A plan lists data and commands but has neither NOT RUN nor a result and claim
  update.

PASS — complete round:
  Question, exact model/controls, training data, confirmation split, linked
  result or NOT RUN, and insight/claim update are all explicit.

FAIL — destructive or duplicative closure:
  A long completed program either deletes full round evidence after writing a
  summary, or copies all full rounds into both the living design and final
  report.

PASS — compacted closure:
  The living design retains a short evidence summary, final claim boundary,
  decision-changing findings, and links. The linked final report or append-only
  ledger preserves every complete round and artifact exactly once.
```
