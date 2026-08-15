---
name: research-exploration
description: Guide problem-first research exploration for ambiguous scientific, systems, ML, robotics, computer vision, or algorithm-design work. Use when Codex must form and refine research questions, conjecture physical or workload structure, turn that structure into mathematical models and computation, select mechanisms from prior art, design falsification and profiling experiments, or update claims from evidence.
---

# Research Exploration

Use this skill to move from an open question to a bounded, falsifiable answer
without confusing world structure, mathematical modeling, computation, and
evidence.

## Communication

Lead with the current question, decision, result, or blocker. Use ordinary
concrete words. Define a technical term where it first appears. Report direct
experimental results as soon as they are available; do not delay them for
viewer or document polish.

Give each active stage one driving question. Keep only the priors, model terms,
mechanisms, and tests needed to answer it. Move a genuinely separate
uncertainty to a later child question instead of growing secondary branches in
the current stage. During early research, language clarity outranks formal
display: add notation only when it makes the driving decision more testable or
less ambiguous.

Before delivering a research document, read it without chat history. Rewrite
every phrase that needs private project context. Formal completeness without
first-reader clarity is `FAIL`.

For a research design, apply the enforceable first-reader clarity contract in
[references/research_documentation.md](references/research_documentation.md)
and audit it with the stage-aware checklist.

## Canonical Workflow

Apply only the steps relevant to the current stage:

```text
research question and scope
-> falsifiable physical or workload priors
-> mathematical decision problem
-> learned-model annex, when parameters are fitted
-> prior-art decision, when a mechanism is being selected
-> constructible computation with prior-to-mechanism traceability
-> smallest distinguishing experiment
-> direct result and stage-level evidence
-> refined question, prior, model, computation, or claim boundary
```

Do not start with an architecture, solver, loss, benchmark, or implementation
unless the researcher has already prescribed it. Do not impose research
artifacts or gates on routine deterministic work.

At every arrow, restate the single driving question in the vocabulary owned by
that stage. If a section cannot be summarized as one question or decision,
narrow it before adding detail.

## Rapid Conjecture Loop (Mandatory)

During question discovery and early design, optimize for learning per unit
time. Before expanding a model or program, record one falsifiable physical or
workload conjecture and the smallest, fastest experiment that distinguishes it.
The record must name:

```text
conjecture or prior
observation that supports it
observation that falsifies or materially refines it
why this test maximizes learning per unit time versus the nearest alternative
exact conjecture update for every declared outcome
```

If any item is missing, the early design is `FAIL`: narrow the question before
adding secondary mechanisms, benchmarks, ablations, or future stages.

## Stage And Artifact Selection

First identify the current deliverable:

| Stage | Required artifact |
|---|---|
| Question discovery | a concise question, importance, scope, and candidate structure |
| Active design | `design.md` or the user-requested equivalent |
| Experiment preparation | a separate experiment contract when commands, schemas, splits, resources, or run receipts become necessary |
| Result interpretation | direct metrics plus evidence appropriate to the claim; add a viewer only when visual inspection matters |
| Stable conclusion | a final synthesis only when the question has a durable bounded answer |

Do not create empty future documents. Keep current theory in the design and
changing run history in an iteration record only when that history is useful.

## Research Design Contract

When writing or revising a research design, read
[references/research_documentation.md](references/research_documentation.md).
Use four sections when computation is fully prescribed or prior art is only
contextual:

```text
1. Problem Definition
2. Physical Priors
3. Mathematical Model
4. Computational Implementation
```

Use five core sections when prior art materially selects, adapts, rejects, or
changes the admissibility of a mechanism:

```text
1. Problem Definition
2. Physical Priors
3. Mathematical Model
4. Related Work and Computational Design Decisions
5. Computational Implementation
```

An active child then uses **Experiments and Iterative Evidence** after the
implementation section—Section 6 in the five-section form. Declare the chosen
structure and reason before drafting.

### Section ownership

- **Problem Definition:** current question, importance, scope, root or parent
  relation, and already revealed child questions. Do not put methods,
  equations, protocols, or changing run status here.
- **Physical Priors:** only falsifiable claims about external world or workload
  structure, their observable consequences, and boundaries. Ask: “Would this
  still be a world claim if no experiment or algorithm existed?” If no, move it.
- **Mathematical Model:** variables, admissible state, constraints derived from
  priors, and the exact decision or optimization objective.
- **Related Work:** only evidence that changes mechanism choice or admissibility,
  plus adopt/adapt/baseline/external-only/reject decisions.
- **Computational Implementation:** the complete selected computation, its
  permitted information, decisions/refusals, and evaluation boundary.
- **Experiments and Iterative Evidence:** a rolling evidence summary followed
  by one scientific record per planned or completed round. Do not introduce a
  new unmodeled mechanism here.

For an active child, name the root priors it inherits or refines. Remove
inactive variants, downstream work, protocol receipts, and duplicate warnings
that do not answer the child question.

## Mathematical Formulation Contract

Every active fixed or learned model must state:

```text
decision or output variable
exact goal, utility, likelihood, posterior, or constrained objective
constraints derived from named physical priors
permitted information and forbidden information
development data allowed to choose an operating point
untouched confirmation evidence and bounded claim
```

A fixed model may have no training loss, but it still needs a decision or
evaluation objective. Desired-property equations and metrics without an exact
decision problem are `FAIL`.

### Learned-model annex

When an active model fits parameters from data, read
[references/learnable_model_completion.md](references/learnable_model_completion.md).
In addition to the base formulation, require observed, latent, learned, and
output variables; the exact trainable objective; admissible state and hard
constraints; anti-collapse and shortcut controls; permitted supervision;
forbidden privileged fields; train/development/confirmation separation; and an
objective-to-computation map. Evaluation-only truth must be inaccessible to
training, checkpoint selection, matching, fitting, and per-example decisions.

Do not force this annex onto an inactive question or fixed diagnostic.

## Prior-Art Decision Contract

When a nontrivial open problem is selecting or adapting a mechanism, read
[references/literature_prior_art_evidence.md](references/literature_prior_art_evidence.md)
after the mathematical constraints and supervision boundary are explicit.

For each representative method, use `Problem -> How it works -> Why ->
Strengths/limits -> Decision`. `How` must say what enters, what the method
measures or constructs, and how that produces the output. `Why` must causally
connect the motivating structure to that computation, not merely name a prior.
Also record supervision, hidden teachers, and boundary compatibility. Prefer
primary sources. A name list, novelty argument, one-sentence mechanism label,
or “self-supervised” claim without tracing its targets is `FAIL`.

Record `NOT_APPLICABLE` only for routine work or a fully prescribed
deterministic mechanism. Prior art cannot replace the mathematical or
implementation contracts.

## Computational Implementation Contract

An active implementation must be detailed enough for an independent
implementer to build the same scientific computation without inventing a
choice. Every outcome-changing design variable must be frozen, included in a
frozen sweep, or marked `BLOCKED`. Keep absolute paths, launch commands,
resource allocation, hashes, and run receipts in the experiment contract.

For every active learnable implementation, use this order unless the document
records an approved exception:

```text
5.1 Implementation purpose and input/output contract
5.2 Prior-to-mechanism design pipeline; each stage uses Goal / How / Why
5.3 Architecture and all frozen design parameters, with concise rationale
5.4 Training computation: candidates, scores/probabilities, loss, optimization,
    and checkpoint selection
5.5 Inference and decision computation: accepted output, refusal, and operating point
5.6 Evaluation boundary, required evidence/artifacts, and link to the detailed
    experiment-control contract
```

Audit each subsection. Missing, swapped, duplicated, or generic subsections are
`FAIL`. A fixed non-learning implementation may use a documented reduced form,
but it must preserve input/output, the prior-to-mechanism map, the exact
algorithm, the decision/refusal rule, and the evaluation boundary.

### Prior-to-inductive-bias traceability

For every active prior, explain:

```text
physical claim
-> mathematical constraint or objective term
-> implementation inductive bias or mechanism
-> why the mechanism promotes the intended behavior
-> remaining failure mode or boundary
```

Put this explanation beside the stage it justifies. Each Section 5.2 stage must
state **Goal** (the uncertainty resolved), **How** (the exact operation and
relevant tensors/state/parameters), and **Why** (the prior, mathematical bias,
intended behavior, and important residual limitation). Do not use a detached
global rationale table that forces the reader to cross-reference the pipeline.

Every significant mechanism must trace back to a prior and mathematical item,
or be labeled as an engineering choice with a practical rationale and no
unsupported scientific claim. A detailed but how-only pipeline is `FAIL`.

Use [references/algorithm_specification.md](references/algorithm_specification.md)
for the separate run-ready experiment contract after the design passes.

## Experiment And Evidence Contract

Before running, define the smallest experiment that distinguishes the current
alternatives. Freeze permitted inputs, forbidden fields, splits, criteria,
status outcomes, metrics, and artifacts. Preserve separate operational,
training, development, and untouched confirmation schemas when applicable.

For each round in the child design, use this reader-facing order:

```text
Question / hypothesis tested
Setup / exact model or baseline version and controlled variables
Training data
Testing or confirmation data and split
Results with linked artifacts/metrics, or explicit NOT RUN
Insight / interpretation, claim-boundary update, and next decision
```

A planned round may record the first four items and `NOT RUN`. A completed
round must contain all six. Never fabricate a result. Keep commands, hashes,
resource receipts, and long machine logs in a linked experiment-control
artifact, but keep the scientific setup, data, result, and insight in the main
design. Maintain one concise rolling summary derived from the rounds rather
than a duplicate status narrative.

### Closure-time evidence compaction

After a child reaches a stable bounded conclusion, compact its living design.
Keep the rolling evidence summary, final claim boundary, decision-changing
findings, and links to the preserved record. Move the complete per-round
question, setup, data, result, and insight records to a linked final report or
append-only evidence ledger. Do not delete evidence, change results, or keep the
same full round history duplicated in both places.

Report the direct result first. Then localize what changed:

```text
invalid measurement
implementation failure
mathematical-model failure
physical-prior failure or boundary violation
research-question failure
insufficient evidence
```

Use [references/profiling_and_evidence.md](references/profiling_and_evidence.md)
for experiment evidence, [references/failure_decomposition.md](references/failure_decomposition.md)
for unresolved failures, and [references/goal_audit.md](references/goal_audit.md)
when the metric no longer matches the downstream purpose.

## Question Refinement

Create child questions only when reasoning or evidence reveals a separable
uncertainty, dependency, coupling, or boundary. Do not generate a large tree in
advance. Keep question, dependency, and coupling relations distinct. Use
[references/problem_discovery.md](references/problem_discovery.md) for a new
problem and [references/problem_refinement.md](references/problem_refinement.md)
for hierarchy changes and evidence propagation.

## Source And Viewer Validation

Write Markdown mathematics only with standard `$...$` inline delimiters and
`$$...$$` display delimiters. Introduce every equation with a plain-language
causal sentence. Put one relation or definition in each display; split long
derivations into named intermediate quantities. Do not use raw LaTeX commands
outside delimiters, deep or nested delimiter constructions, or continuation
lines that begin with an operator such as `+`, `-`, or `=`.

Always run `scripts/check_markdown_math.py` on every changed Markdown research
file that contains mathematics. A failure blocks delivery. A source pass is
not proof of rendering.

When rendered mathematics is a requested deliverable or the named primary
viewer is available, probe one inline and one display expression in that exact
viewer, then inspect the final occurrences. If the viewer is unavailable,
report rendering as unverified; do not rewrite delimiters blindly or block
unrelated scientific work.

Create a research viewer only when visual evidence materially helps interpret
a result. Then read
[references/research_viewer_design.md](references/research_viewer_design.md),
write the plot contract before plotting, and perform one bounded rendered
audit. Do not require a viewer for design-only work or nonvisual evidence.

## Final Audit

Use [references/research_loop_checklist.md](references/research_loop_checklist.md).
Return `FAIL` before implementation or delivery when an applicable contract is
incomplete. Do not make an inactive future stage choose a model, loss, dataset,
or threshold.

## Reference Routing

- `research_documentation.md`: document ownership, mathematical base contract,
  computation structure, traceability, artifacts, and source/render rules.
- `learnable_model_completion.md`: conditional learned-model annex.
- `literature_prior_art_evidence.md`: conditional source search and mechanism
  decision record.
- `algorithm_specification.md`: run-ready algorithm and experiment contract.
- `profiling_and_evidence.md`: metrics, examples, artifacts, and interpretation.
- `failure_decomposition.md`: localize a broad failure.
- `goal_audit.md`: reconsider a repeatedly failing goal or metric.
- `problem_discovery.md`: establish a new question and candidate structure.
- `problem_refinement.md`: maintain hierarchy and propagate evidence.
- `research_viewer_design.md`: conditional plot/viewer contract.
- `research_loop_checklist.md`: final stage-aware audit and regression fixtures.
- `latex_toolchain.md`: build and audit a LaTeX paper.
