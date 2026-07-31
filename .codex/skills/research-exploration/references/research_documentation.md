# Research Documentation

Use this reference when writing or revising a research document.

## Contents

1. Separate current state from history
2. Write the four-part testable argument
3. Complete active learnable mathematical models
4. Maintain the program research map
5. Record each iteration
6. Map equations and parameters to evidence

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
   variables, state, relations, constraints, and testable predictions
   for an active selected learnable model: the completion-gate contract
   for a fixed baseline: the explicit no-learnable-objective declaration
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

## Active Learnable Mathematical Models

When an active stage selects a learnable representation, dynamics model,
estimator, or policy, read
[learnable_model_completion.md](learnable_model_completion.md) and record an
explicit `PASS` or `FAIL` for its completion gate. The Mathematical Model must
define the observed, latent, learned, and output variables; exact constrained
objective or declared likelihood/posterior objective; admissible state and hard
constraints; known degenerate or shortcut solutions and their exclusions;
permitted supervision and forbidden fields; training versus untouched held-out
terms; and the objective-to-code/artifact map.

Desired-property equations and evaluation residuals do not substitute for the
objective that fits the learnable parameters. Conversely, do not add a loss to
an inactive question or fixed diagnostic baseline. For an active fixed
baseline, state `learnable objective: none`, the mechanism isolated, the claim
boundary, and which later learnable stage will need the gate.

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

For an active learnable model, every objective term and hard constraint must
also map to its permitted training fields, exact code path, logged training
artifact, and distinct held-out falsification artifact. If the document claims
to learn a representation but has no optimized variables and no constrained
objective, the mathematical-model review fails even when the source contains
equations and evaluation tests.

For Markdown research documents, distinguish the LaTeX expression from the
Markdown container and from the renderer. Delimiters are viewer-specific:
`$...$`, standalone `$$`, `\(...\)`, `\[...\]`, and fenced blocks are not
interchangeable, and no one form is a safe universal default.

Use this rendering workflow:

1. Name the primary viewing surface precisely, including the application,
   extension or renderer, and version when known.
2. In a disposable file of the same type, test one representative inline
   expression and one representative multiline display expression.
3. Open that probe in the primary viewer. Record which container syntax
   rendered successfully and retain a screenshot or equivalent evidence.
4. Only after the probe passes, apply that syntax to the full document.
5. Run `scripts/check_markdown_math.py <changed-markdown-files>` to inventory
   the math and check source structure. Its success is a source pass, not a
   rendering pass.
6. Open the final document in the same viewer and inspect every inline and
   display occurrence. Compare the count with the source inventory.
7. Fail the render audit if any command or delimiter is visible, an equation is
   styled as code, a parse error appears, or notation is clipped or overflows.
8. Record a render receipt with the viewer, version when known, syntax,
   equation counts, checker command/result, evidence, and final `RENDER PASS`
   or `RENDER FAIL`.

The source checker inventories recognized containers without assuming that any
of them render. After a viewer probe succeeds, its optional profile can make
the checker reject containers that were not verified:

```json
{
  "viewer": "application, renderer or extension, and version",
  "verified_on": "YYYY-MM-DD",
  "evidence": "render-receipt or screenshot path",
  "inline_containers": ["dollar"],
  "display_containers": ["double-dollar"]
}
```

Run the profile-aware check as:

```text
scripts/check_markdown_math.py \
  --profile-file <viewer-profile.json> \
  <changed-markdown-files>
```

Recognized inline container names are `dollar` and `parenthesis`. Recognized
display names are `double-dollar`, `double-dollar-inline`, `bracket`,
`bracket-inline`, `fenced-math`, `fenced-latex`, and `fenced-tex`. A fenced
container is acceptable only when the target viewer probe and profile permit
that exact form. A profile records the result of a render probe; it does not
replace the final visual audit.

If the exact target viewer is unavailable or automation cannot inspect it, say
that rendering remains incomplete. If none of the minimal probes renders,
preserve the LaTeX source, stop before bulk conversion, and offer an alternate
verified artifact or viewer. Never infer successful rendering from balanced
delimiters, from a source checker, or from a different rendering surface.

Every hyperparameter must have:

```text
name
value
definition
reason for this value
effect if too low or too high, when useful
```

Write simply. Rigor means precise, not fancy.
