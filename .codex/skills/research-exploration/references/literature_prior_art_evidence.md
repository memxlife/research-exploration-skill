# Literature / Prior-Art Evidence

Use this reference after the mathematical constraints are explicit and before
selecting or adapting a computational mechanism for a nontrivial open research
problem.

## Contents

1. Decide whether the gate applies
2. Search from the research question and model
3. Record evidence for each retained mechanism
4. Classify practical roles and hidden supervision
5. Write the implementation decision record
6. Keep documentation proportional
7. Review the gate result
8. Run the forward scenarios

## Trigger

Apply the gate when all of the following hold:

1. the work is a nontrivial open or ambiguous research problem;
2. the current question, physical priors, mathematical constraints, and
   supervision or no-leakage boundary are explicit; and
3. the work is about to select, adapt, compare, or reject a computational
   mechanism.

The gate applies to fixed and learned candidate selection. It does not apply to
routine non-research work or to a fully prescribed deterministic baseline whose
algorithm has already been selected by the researcher or an accepted upstream
contract. Record that reason instead of inventing a search.

## Search From The Question And Model

Search for the smallest question that can change the implementation decision.
Use the mathematical constraints and supervision boundary as search terms, not
only the project name or proposed architecture.

Use this order:

1. Freeze the research question, physical structure, predicted consequence,
   mathematical constraints, and permitted/forbidden information.
2. Search the directly affected scientific and engineering literatures.
3. Prefer original papers, official technical reports, standards, datasets,
   and authoritative project documentation. Use a survey to discover sources,
   then cite the primary source when available.
4. Seek counterexamples, negative results, boundary conditions, and known
   shortcuts in addition to supportive work.
5. Distinguish what the source directly demonstrates from the inference that a
   mechanism may help the current problem.
6. Stop when the retained evidence is sufficient to choose the fastest
   falsifiable baseline and identify material alternatives; do not turn the
   gate into an unbounded novelty search.

## Per-Mechanism Evidence Record

For every retained mechanism, record all fields below:

| Field | Required content |
|---|---|
| Source | Primary citation or the best available authoritative source |
| Exact problem | The input, output, and question the cited work actually addresses |
| Physical structure | The regularity exploited, such as locality, continuity, sparsity, symmetry, geometry, common motion, or hierarchy |
| Demonstrated role or benefit | What the source measured or established, with the tested scope |
| Assumptions | Sensor, observability, scene, dynamics, coordinate, computational, and deployment assumptions |
| Supervision and cost | Labels, pseudo-labels, pretraining, demonstrations, trajectories, simulation, data collection, and relevant compute |
| Failure or counterexample | Known ambiguity, degeneracy, domain boundary, shortcut, or negative result |
| Boundary compatibility | Exact agreement or conflict with permitted supervision, forbidden fields, causal cutoff, and held-out evidence |
| Role classification | Boundary-compatible baseline, adaptation candidate, external upper bound/diagnostic, or context only |
| Decision | Adopt, adapt, reject, defer, or retain only as an ablation, with the reason |

Do not write “self-supervised” as a supervision description. Inspect how
positives, targets, tracks, masks, visibility, geometry, rewards, and checkpoint
criteria were produced.

## Role Classification

- **Boundary-compatible baseline:** can operate within the declared inputs,
  supervision, causal, and no-leakage contract.
- **Adaptation candidate:** exploits useful structure, but a published input,
  objective, teacher, data source, or output must change.
- **External upper bound / diagnostic:** may quantify what privileged
  information buys, but cannot train, tune, filter, or validate the core path.
- **Context only:** clarifies a principle, failure, or neighboring task without
  supplying the selected computation.

A method can be boundary-compatible and still solve only a partial analogue of
the current problem. Record supervision compatibility and problem match as
separate judgments.

## Hidden Oracle Audit

Inspect both training and selection pipelines for information that may be
hidden behind “automatic,” “synthetic,” “reconstructed,” or “self-supervised”:

```text
ground-truth pose, trajectory, transform, correspondence, track or visibility
depth, masks, segmentation, identity, object state or simulator state
optical-flow, SfM, SLAM, reconstruction or synthetic-warp teachers
human demonstrations, success labels, rewards, resets or curated negatives
web, foundation-model or robot-data pretraining and its compute
future observations, held-out labels or evaluation data used for tuning
fit evidence reused as independent validation
a decoder or downstream policy that can hide failure of the claimed mechanism
```

Privileged information may remain in a physically separate evaluation artifact
or external comparator. It must not enter the core learner, candidate generator,
threshold tuner, checkpoint selector, fit, rejection gate, or held-out test.

## Implementation Decision Record

Before writing or revising the computational implementation, record:

```text
research question and mathematical constraints
search scope and retrieval date
supervision and no-leakage boundary
retained mechanism table
adopted baseline and the physical structure it exploits
adaptations required for the current boundary
rejected or external-only mechanisms and reasons
fastest falsifiable baseline and the first ablations
remaining literature uncertainty that could change the decision
gate result: PASS, FAIL, or NOT_APPLICABLE
```

The Computational Implementation must cite this record or its exact subsection
and state which decision it realizes. A selected mechanism with no cited
decision record is blocked.

Practical leverage and novelty are different questions. First decide which
existing mechanism most efficiently tests the research conjecture. Mention
novelty only as a bounded source-comparison note; lack of a found precedent is
not proof of novelty.

## Proportional Documentation

Keep a compact decision table inside the four-part design when the evidence is
small. Create one bounded standalone literature receipt or report when the
source set, supervision audit, or comparison materially exceeds the design's
scope. Link it from Computational Implementation.

Do not create a mandatory fifth top-level design section. Do not proliferate
documents when the researcher asked for one design document: in that case,
place the compact decision record inside the Computational Implementation or a
clearly marked appendix of that same document.

## Gate Review

Return one explicit result:

- **PASS:** the targeted search, per-mechanism evidence, classification,
  hidden-oracle audit, decision, and implementation citation are complete.
- **FAIL:** a nontrivial selected or adapted mechanism lacks any required field,
  has an unresolved supervision conflict, or is not backed by a cited decision
  record. Do not implement while the gate fails.
- **NOT_APPLICABLE:** the task is routine non-research work or a fully
  prescribed deterministic baseline. State who or what prescribed it and why
  no mechanism-selection decision is being made.

For an active learnable model, this gate and the Learnable-Model Completion Gate
must pass independently. Prior art cannot replace the exact learnable objective,
constraints, anti-shortcut controls, schemas, or objective-to-code map. A
complete learnable model also cannot justify an uninformed mechanism choice.

## Forward Scenarios

### Positive

An active local-descriptor question has explicit invariance, separation,
geometry, and no-pose/no-correspondence constraints. The researcher compares a
fixed descriptor, a raw-video cycle learner, and a pose/depth-supervised matcher
using primary sources. The record classifies them respectively as a
boundary-compatible baseline, adaptation candidate, and external upper bound;
records their failures; adopts the fixed baseline as the first falsification;
and the implementation cites the record.

Expected result: **PASS**.

### Negative

An active research design selects a learned matcher after writing desired
equivariance equations, but it contains no targeted source search, no account of
how published matches were produced, and no adopted/adapted/rejected decision.

Expected result: **FAIL** even if the Learnable-Model Completion Gate passes.

### Hidden-oracle negative

A paper calls its method self-supervised, but its positives come from known
camera pose, reconstructed depth, optical flow, or a synthetic warp. The current
contract forbids those teachers, yet the implementation adopts the method as a
core learner without adaptation.

Expected result: **FAIL**. Reclassify it as an external upper bound or redesign
the supervision.

### False-positive guard

The researcher explicitly prescribes a deterministic checksum or a fixed
closed-form baseline, and no mechanism choice or adaptation is occurring.

Expected result: **NOT_APPLICABLE** with the prescription recorded.
