# Stage-Aware Research Audit

Use only the blocks that apply to the current stage. Any applicable missing
contract is `FAIL`; an inactive future stage is not required to choose a model,
loss, dataset, or threshold.

## Fast Delivery Audit

Return `FAIL` and revise before delivery if any answer is no:

1. Does the document focus on the most important driving problem using the
   smallest useful model?
2. Could a PhD-level reader outside the immediate specialty explain the causal
   idea after one careful reading?
3. Could that reader reconstruct the complete chain from motivation and local
   definitions through the derivation to its conclusion, implication, and
   limitation without chat history?

Also return `FAIL` if any answer is no:

- Does every active stage name one driving question or decision?
- Were secondary branches removed, deferred, or promoted to their own child
  question?
- Does early work name one falsifiable conjecture or prior and the smallest,
  fastest experiment that distinguishes it?
- Are the supporting observation, falsifying or refining observation, and exact
  conjecture update for every declared outcome stated before expansion?
- Does the design explain why this test maximizes learning per unit time over
  the nearest alternative?
- Does every display follow a plain-language causal sentence and contain only
  one relation or definition?
- Are long formulas split into named intermediates, with no deep or nested
  construction and no continuation line beginning with `+`, `-`, or `=`?
- Does Markdown math use only `$...$` and `$$...$$`, with no raw LaTeX outside
  delimiters?
- Did every changed Markdown research file containing math pass
  `scripts/check_markdown_math.py`?

## Question And Document

- Is the current question stated before any mechanism?
- Does each active stage state one driving question or decision?
- Were secondary concerns removed when they do not change the current test?
- Are importance, scope, parent/root relation, and already revealed children
  clear without chat history?
- Is the compact, four-, or five-section structure proportional to the current
  question, with no empty or unnecessary sections?
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

## First-Reader Clarity

Read the document without chat history, source code, or earlier drafts.

- Does the document read as self-contained, insightful research prose for a
  PhD-level reader outside the immediate specialty, unless the user requested
  another audience or format?

- Can the reader state the research question and scope in ordinary words?
- Can the reader identify the world or workload assumptions and their limits?
- Can the reader explain the mathematical objective and prior-derived
  constraints without decoding unexplained notation?
- Can the reader explain every implementation stage's Goal, How, and Why?
- Can the reader find the direct result or explicit `NOT RUN` state?
- Can the reader distinguish what the evidence supports, does not support, and
  leaves unresolved?
- Are technical terms, symbols, abbreviations, and internal IDs defined at first
  use rather than used as substitutes for explanation?
- Were context-dependent phrases, abstract nominalizations, unnecessary tables,
  caveat chains, and repeated disclaimers removed or rewritten directly?

Return `FAIL` before delivery if formal completeness is present but any of these
answers still requires private project context.

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
- For a claimed causal comparison, are the exact compared objects and update or
  perturbation formulas stated separately for both sides?
- Are direct method-to-method measurements distinguished from target-based
  quality measurements?
- Were parameter shapes, input and output dimensions, normalization,
  aggregation, gradient or perturbation geometry, starting behavior, data, and
  randomness audited before attributing the difference to one factor?
- If more than one relevant factor changed, was the smallest matched control
  added, or did the document state that the comparison cannot isolate one
  cause?
- Was each scaling law derived from its own model rather than transferred by
  analogy, including any power introduced mechanically by normalization?
- Does a failed baseline, approximation, pairing, or numerical check produce
  an inconclusive result rather than support or falsification?
- For early work, are support, falsification or refinement, and insufficient-
  evidence outcomes each mapped to an exact next conjecture rather than only a
  status label?
- Is the learning-per-unit-time rationale concrete enough to justify deferring
  the nearest slower or broader test?
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
- Does source math use only `$...$` and `$$...$$`?
- Does a plain-language causal sentence introduce every display?
- Does each display contain one relation or definition, with named
  intermediates replacing deep or nested expressions?
- Are line-leading operators and raw LaTeX outside delimiters absent?
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

FAIL — formal but unreadable:
  A cold reader sees “PR7,” “admissible z,” “M1,” and “R3 PASS,” but cannot tell
  the world assumption, optimized decision, computation, measured result, or
  claim boundary without asking for prior project context.

PASS — reader-complete:
  The question and assumptions are stated directly; the objective and
  constraints are explained before notation; every stage gives Goal, How, and
  Why; the result and its boundary are explicit; and every necessary term or
  label is defined at first use.

FAIL — renderer-fragile math:
  A large nested display combines several definitions, begins continuation
  lines with operators, or contains raw LaTeX outside `$...$` or `$$...$$`.

PASS — renderer-safe math:
  A causal sentence introduces one definition; named intermediate quantities
  use separate `$$...$$` displays; each display is explained in plain language;
  and `scripts/check_markdown_math.py` passes.

FAIL — broad early program without a conjecture loop:
  An early design proposes several models, datasets, ablations, and future
  stages but never names the one conjecture, discriminating observations,
  learning-per-time rationale, or exact update after each outcome.

PASS — rapid conjecture loop:
  One conjecture names its supporting and falsifying observations; the shortest
  distinguishing test is justified against the nearest alternative; and every
  outcome produces a specific revised conjecture or bounded stop decision.

FAIL — causal attribution from unmatched systems:
  Two experiments use different losses, parameter shapes, normalizations, and
  random-update geometry, yet the result is attributed to the loss alone.

PASS — matched mechanism comparison:
  The comparison states both update-noise formulas, keeps the starting
  input-output behavior and evaluation fixed, changes one proposed cause, and
  treats a failed approximation check as inconclusive.
```
