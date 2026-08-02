# Prior-Art And Mechanism Decision

Use this reference after the question, mathematical constraints, and
supervision boundary are explicit and before selecting or adapting a mechanism
for a nontrivial open problem.

## Trigger

Apply it when prior work can change the selected mechanism, required
adaptation, or admissibility. Record `NOT APPLICABLE` for routine work or a
fully researcher-prescribed deterministic mechanism; name the prescription.

## Targeted Search

Search for the smallest source question that can change the implementation.
Prefer primary papers, official technical reports, standards, datasets, and
authoritative project documentation. Use surveys to find primary sources.

Search from:

```text
current research question
physical priors and mathematical constraints
permitted and forbidden information
candidate mechanism families
known ambiguity, shortcut, or counterexample
```

Seek negative results and boundary conditions as well as supportive work. Stop
when the evidence can select the fastest falsifiable baseline and identify the
material alternatives; do not turn this into an unbounded novelty search.

## Decision-Relevant Method Families

For every representative method or genuinely equivalent family that changes a
decision, explain in plain language:

| Item | Required explanation |
|---|---|
| Source | primary or best authoritative citation |
| Problem | what input, output, and question the work actually addresses |
| How it works | what enters; what the method measures, constructs, or updates; and how that computation produces its output |
| Why | the causal reason the motivating structure makes that computation useful; naming locality, continuity, geometry, or another prior without the causal link is insufficient |
| Demonstrated strengths | what the source measured and within what scope |
| Assumptions and cost | sensors, scene, compute, pretraining, data, or deployment assumptions |
| Supervision | how positives, targets, tracks, rewards, or labels are produced |
| Failure and boundary | ambiguity, shortcut, counterexample, or domain limit |
| Compatibility | exact agreement or conflict with the current causal and no-leakage boundary |
| Decision | adopt, adapt, baseline, external-only, reject, or defer, and why |

Present each representative in this reader order: **Problem**, **How it
works**, **Why**, **Strengths and limits**, and **Decision**. Group minor
variants only when they solve the same problem by materially the same mechanism.
Do not name a method that the reader cannot understand without opening its
paper. A citation list, one-sentence mechanism label, generic pros/cons, or
novelty prose is `FAIL`. Use formulas only when they make the computation easier
to understand than ordinary language.

## Hidden-Teacher Audit

Do not accept “self-supervised” as a supervision description. Inspect whether
training, selection, or filtering uses:

```text
pose, trajectory, transform, correspondence, tracks, or visibility
depth, masks, segmentation, identity, object or simulator state
optical flow, SfM, SLAM, reconstruction, or synthetic warps
demonstrations, rewards, resets, success labels, or curated negatives
foundation-model or web pretraining and its cost
future observations or held-out labels used for tuning
fit evidence reused as independent confirmation
a decoder or downstream policy that can hide failure of the claimed mechanism
```

Privileged information may be an external upper bound or physically separate
confirmation artifact. It may not enter the core learner, pseudo-labels,
candidate generator, checkpoint selector, fitter, threshold tuner, or
per-example decision when the design forbids it.

## Role And Decision Record

Classify each retained family:

- **boundary-compatible baseline:** usable under the declared boundary;
- **adaptation candidate:** useful structure, but published supervision or
  computation must change;
- **external-only:** privileged upper bound or diagnostic;
- **context only:** explains a principle or failure but supplies no mechanism.

Section 4 of a five-section design owns the concise explanation and direct
decision. A larger standalone receipt is optional only when needed for
readability; Section 4 still links it and records the adopted decision. Section
5 cites and implements that decision.

Practical leverage comes first. Failure to find a precedent is not proof of
novelty.

## Result

- **PASS:** the targeted search, explanatory method records, hidden-teacher
  audit, roles, decisions, and Section 5 handoff are complete.
- **FAIL:** a selected mechanism lacks evidence, has an unresolved supervision
  conflict, is only name-listed, or is not connected to an implementation
  decision.
- **NOT APPLICABLE:** routine work or a fully prescribed deterministic
  mechanism, with the source of prescription recorded.

## Forward Checks

```text
FAIL: “Use SIFT, TimeCycle, and LoFTR. TimeCycle is self-supervised and LoFTR
      is strong.” No problem, mechanism, teacher, limitation, or decision is
      explained.

FAIL: “Shi--Tomasi scores two-dimensional gradient structure.” The sentence
      names a measured object but does not explain the input, computation, or
      how the score produces selected corners.

PASS: Shi--Tomasi takes a small image window, builds the local structure tensor
      from horizontal and vertical intensity gradients, and keeps points whose
      two eigenvalues are both strong. Two strong directional changes indicate
      a corner whose motion can be constrained in both image directions; an
      edge remains ambiguous along the edge.

PASS: A raw-video cycle method is explained as temporal return consistency
      without a pose teacher; repeated texture can close a wrong cycle; the
      design therefore adapts the cycle signal and adds local alternatives,
      refusal, and held-out checks.

FAIL: A published “self-supervised” matcher uses known camera pose or depth to
      create targets, but the current core path adopts it despite forbidding
      those fields.

NOT APPLICABLE: The researcher prescribed a fixed checksum and no mechanism
      selection or adaptation is occurring.
```
