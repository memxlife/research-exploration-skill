# Research Design Contract

Use this reference when writing or reviewing an active research design.

## Contents

1. Choose the document structure
2. Enforce section ownership
3. Complete the mathematical model
4. Complete the computational implementation
5. Keep artifacts proportional to the stage
6. Enforce first-reader clarity and validate mathematics and rendering
7. Run forward checks

## Choose The Structure

Record the choice before drafting:

```text
design structure: FOUR_SECTION_ALLOWED | FIVE_SECTION_REQUIRED
reason: whether prior art materially changes mechanism choice, adaptation,
        or admissibility
```

Use four core sections for a fully prescribed fixed mechanism or contextual
prior art. Use five core sections when prior art materially selects, adapts,
rejects, or changes a mechanism's admissibility. An active child then appends
`Experiments and Iterative Evidence` after computation—Section 6 in the
five-section form.

## Section Ownership

Before drafting details, write one driving question or decision for each active
section. Include only material that changes that answer. A second independent
question belongs in a new child or later study, not as a branch inside the
current section.

| Section | Owns | Must not contain |
|---|---|---|
| 1. Problem Definition | selected question, importance, scope, parent/root relation, already revealed children | priors, equations, methods, protocol, or changing run status |
| 2. Physical Priors | falsifiable external world/workload claims, observable consequences, scope and boundaries | algorithms, thresholds, candidate policies, splits, leakage controls, or evaluation rules |
| 3. Mathematical Model | variables, admissible state, prior-derived constraints, exact decision or optimization objective | architecture, pipeline, commands, artifacts, literature narrative, or run status |
| 4. Related Work and Computational Design Decisions | decision-relevant prior work, supervision and hidden-teacher audit, adopt/adapt/baseline/external-only/reject decisions | full mathematics, full pipeline, or claims of new experimental results |
| 5. Computational Implementation | permitted inputs, outputs, causal mechanism map, architecture, training/inference computation, refusal, and evaluation boundary | inactive future branches, raw commands, hashes, resource allocation, or long run history |
| 6. Experiments and Iterative Evidence | rolling evidence summary; one scientific record per planned/completed round; claim update and next decision | fabricated results, unmodeled mechanisms, or raw control-plane logs |

In a four-section design, implementation is Section 4 and keeps the same owner.
Record the prior-art decision as `NOT_APPLICABLE` or contextual immediately
before it.

### Physical-prior purity

Ask of every proposed prior:

> Would this still be a claim about the world or workload if no experiment or
> algorithm were ever designed?

If no, move it. Candidate generation, independent recomputation, thresholds,
data splits, leakage controls, held-out logic, validation rules, and status
precedence belong to mathematics, implementation, or the experiment contract.

### Child scope

An active child names the root priors it inherits or refines. Every section
answers that child question only. Remove inactive future variants, downstream
stages, duplicate no-leakage warnings, experiment manifests, and current status
from sections that do not own them. Keep one causal chain consistent across the
document.

## Mathematical Model

Every active fixed or learned model states:

```text
observed inputs and decision/output variables
latent or inferred state, when any
admissible state and hard constraints
exact goal, utility, likelihood, posterior, or constrained objective
which physical prior gives rise to each constraint or term
permitted and forbidden information
development data allowed to select an operating point
untouched confirmation metrics and bounded claim
```

A fixed model may have no training loss. It still needs an exact decision or
evaluation objective. For example, development data may choose the strictness
that maximizes accepted correct-match coverage subject to a precision
requirement chosen before the experiment, followed by one untouched
confirmation report.

Return `FAIL` when equations describe desired properties or tests but never
state what decision is optimized under which constraints.

### Learned-model annex

When parameters are fitted from data, also apply
[learnable_model_completion.md](learnable_model_completion.md). The mathematical
model must include trainable variables, exact objective terms and aggregation,
hard constraints, known shortcut or collapse solutions, their exclusions,
permitted supervision, forbidden privileged fields, disjoint training and
held-out roles, and the objective-to-computation map.

Operational, training, development, and confirmation information must be
separate. Evaluation-only truth cannot enter gradients, pseudo-labels,
checkpoint selection, candidate construction, matching, fitting, threshold
selection for an untouched claim, or a per-example decision.

## Prior-Art Decision

If selecting or adapting a nontrivial mechanism, apply
[literature_prior_art_evidence.md](literature_prior_art_evidence.md) after the
mathematical and supervision boundaries are explicit. Section 4 must explain
the methods that actually change the decision and end with direct decisions.
Do not use a citation list or novelty discussion as a substitute.

## Computational Implementation

The implementation must let an independent reader build the same scientific
computation without inventing an outcome-changing choice. Freeze every such
choice, define a frozen sweep and its selection rule, or mark the implementation
`BLOCKED` with the missing decision.

### Required order for an active learnable implementation

Use this order unless an approved exception is documented:

#### 5.1 Implementation purpose and input/output contract

State the capability being implemented; tensor, state, and unit meanings;
permitted and forbidden inputs; and output/refusal types.

#### 5.2 Prior-to-mechanism design pipeline

Describe the computation in its causal order. Every stage uses the same local
structure:

```text
Stage name
Goal: the uncertainty or subproblem this stage resolves.
How: the exact operation, tensors or state, and relevant parameters.
Why: the physical prior and mathematical constraint/objective behind the
     inductive bias, the behavior it promotes, and an important residual
     limitation when one exists.
```

The `Why` carries the full trace from physical claim to mathematical item to
inductive bias to concrete mechanism. Keep it beside the operation it explains;
do not replace it with a detached global rationale table or symbol crosswalk.
Audit in reverse: every significant mechanism must trace to a prior and
mathematical item, or be labeled `engineering` with a practical rationale and
no scientific claim.

#### 5.3 Architecture and frozen design parameters

Specify input encoding, model components and sharing, dimensions, candidate
geometry, constraints, and every scientific or architectural value needed for
the first implementation. Give a concise prior/model/evidence rationale or
label the value as a preregistered engineering baseline. A sweep freezes its
range, selection data, rule, and rationale.

#### 5.4 Training computation

State candidate and batch construction, scores or probabilities, exact loss
terms and weights, constraint enforcement, optimizer and schedule, stop rule,
validation, and checkpoint selection. Map each training computation back to a
Section 3 item.

#### 5.5 Inference and decision computation

State the ordered inference algorithm, operating-point selection, accepted
output, refusal/error/break behavior, collision or consistency rules, and state
passed downstream.

#### 5.6 Evaluation boundary and evidence

State what remains frozen, what evaluator-only truth may inspect after the
decision, final metrics, observable diagnostic artifacts, and the link to the
detailed experiment-control contract. Keep commands, absolute paths, hashes,
resource allocation, and run receipts out of the design.

Return `FAIL` for a missing, swapped, duplicated, or generic subsection. A
component list such as “shared CNN produces descriptors” is not constructible.

### Reduced fixed implementation

A fixed non-learning implementation may use fewer subsections if the exception
is stated. It must still contain: purpose and input/output; prior-to-mechanism
trace; complete algorithm and frozen values; accepted/refusal behavior; and
evaluation boundary.

## Stage-Conditional Artifacts

Create only what the current stage uses:

- **Design-ready:** one current design; no experiment or viewer is required.
- **Run-ready:** add an experiment contract with data schema, splits, exact
  command/configuration, criteria, resource needs, and artifact paths.
- **Result-ready:** preserve direct metrics and evidence appropriate to the
  claim. Add visual examples or a viewer when the phenomenon is visual,
  spatial, temporal, or otherwise easier to inspect visually.
- **Close-ready:** add final synthesis only when the bounded answer is stable.

Use an iteration ledger or research map only when durable history or multiple
active nodes make it useful. Do not create empty child directories or duplicate
editable answers.

## Experiments And Iterative Evidence

Begin Section 6 with a concise rolling summary of what the recorded rounds
currently support, what remains unknown, and the immediate decision. Derive the
summary from the rounds; do not maintain a second independent status account.

Use the same structure for every round:

```text
Question / hypothesis tested
Setup / exact model or baseline version and controlled variables
Training data
Testing or confirmation data and split
Results: linked artifacts and metrics, or explicit NOT RUN
Insight / interpretation, claim-boundary update, and next decision
```

A planned round may contain the first four items and `NOT RUN`; its final item
states the blocker or approval needed. A completed round contains all six and
must link its evidence. Never infer or fabricate results from a plan.

Commands, hashes, machine allocation, environment receipts, and long logs may
remain in a linked experiment-control document. The main design still carries
the scientific setup, training data, confirmation data, result, interpretation,
and resulting claim boundary for every round.

### Closure-time evidence compaction

The rule above applies while the child is active and its answer is changing.
After the child reaches a stable bounded conclusion, the living design keeps:

```text
short rolling evidence summary
final claim boundary
findings that changed the selected model, mechanism, or conclusion
links to the complete preserved round records and artifacts
```

Move the full per-round question, setup, data, result, and insight records to a
linked final report or append-only evidence ledger. Preserve every round and
its artifacts; compaction is not deletion or reinterpretation. Do not retain the
same complete history in both the living design and the linked record.

## Plain-Language And First-Reader Clarity Contract

Audit the document as a reader who has not seen the chat, code, or earlier
drafts. The reader must be able to identify, in ordinary words:

```text
the research question and its scope
the world or workload assumptions
the mathematical decision or optimization objective and its constraints
each implementation stage's Goal, How, and Why
the observed or NOT RUN result
the supported claim, unsupported claim, and remaining boundary
```

### Undergraduate-textbook default

Unless the user names another audience or format, every design document,
research note, proof, and derivation must teach its subject at the level of a
first-year undergraduate textbook. This is a rigor requirement, not a request
to remove mathematics. The document must:

- state the motivating question before presenting a method or equation;
- give all background needed to understand the setup;
- define every term and symbol before its first use;
- explain why each equation is introduced and how each derivation step follows;
- carry the mathematics through to a concrete conclusion rather than stopping
  at a setup equation;
- explain what the conclusion means, when it applies, and when it does not;
- remain understandable without Codex adding a separate explanation in chat.

A mathematically correct document that fails any item above is `FAIL` and must
be rewritten before delivery.

Use these writing rules:

- Begin every section with its single driving question, decision, or result.
  Remove secondary concerns that do not change the current experiment.
- Lead each section with the concrete question, claim, operation, result, or
  decision it owns.
- Use direct subjects and actions. Prefer “the matcher refuses this candidate”
  to an abstract phrase such as “rejection is instantiated.”
- Define each necessary technical term, symbol, abbreviation, and internal ID
  at first use. A label may support navigation; it may not carry the explanation.
- Replace context-dependent phrases such as “the current route,” “this signal,”
  “the above mechanism,” or “valid support” with the exact object or a nearby
  definition when a cold reader could interpret them more than one way.
- State the physical or causal idea before its equation or implementation
  detail. Mathematics must sharpen an understood claim, not hide a missing
  explanation.
- During question discovery and active design, prefer a short causal
  explanation over a formally complete display that does not change a
  decision. Defer formal detail to a run-ready contract when it becomes needed.
- Prefer one main idea per sentence; split a sentence when doing so makes the
  logic clearer. Remove examples, tables, labels, caveat chains, and repeated
  disclaimers that do not make the explanation clearer.
- Keep detail in the section that owns it; do not make an overview readable only
  by chasing implementation or experiment-control artifacts.

Return `PASS` only when the cold reader can answer all six reader questions
without private project context. Return `FAIL` and repair before delivery when
the document is formally complete but its question, assumptions, objective,
computation, result, or boundary cannot be explained in plain language.

## Mathematics And Rendering

Use only standard `$...$` for inline mathematics and `$$...$$` for display
mathematics. Introduce each equation with a plain-language causal sentence.
Keep one relation or definition per display. When a formula needs multiple
steps, define short named intermediates in separate displays and explain each
one immediately afterward.

Do not use raw LaTeX commands outside math delimiters, `\(...\)`, `\[...\]`,
fenced math blocks, deep or nested delimiter constructions, or visually fragile
continuations whose first non-space character is `+`, `-`, or `=`. Do not use
equation layout as a substitute for a causal explanation.

For every changed Markdown file containing mathematics, always run:

```text
scripts/check_markdown_math.py <changed-markdown-files>
```

Any source-validation failure is `FAIL` and blocks delivery. A source pass does
not prove rendering. When rendered mathematics is requested or the named
primary viewer is available, test one
inline and one display expression in that exact viewer, then inspect the final
occurrences for raw commands, code styling, parse errors, clipping, and
overflow. If the viewer is unavailable, report rendering as unverified and
continue scientific work that does not depend on that rendering.

## Forward Checks

```text
FAIL — prior purity:
  “Use a held-out split” appears as a physical prior.

FAIL — mathematical formulation:
  A fixed matcher has ranking equations but no precision-versus-coverage goal.

FAIL — learned annex:
  A representation has desired invariance equations but no trainable objective,
  supervision boundary, anti-collapse control, or held-out separation.

FAIL — constructibility:
  “A shared CNN produces unit descriptors, then matches them.”

FAIL — traceability:
  A detailed step list contains a local window but gives only How. It never
  states the Goal, explains that continuity gives a bounded displacement, or
  says when the true match can fall outside.

PASS — traceability:
  Goal: restrict correspondence uncertainty under bounded motion.
  How: apply the frozen local candidate mask.
  Why: continuity -> displacement bound -> local mask -> distant candidates
  cannot win; fast motion or occlusion may invalidate the mask.

FAIL — ownership:
  Section 3 contains architecture, commands, current run status, and future
  downstream stages.

FAIL — incomplete experiment record:
  A results-only table omits the hypothesis, controlled setup, data, and
  interpretation; or a protocol-only plan silently appears completed.

PASS — experiment round:
  The round states its question, exact model/controls, training data,
  confirmation split, linked result or NOT RUN, and insight/claim update.

FAIL — closed-program evidence history:
  A stable child either replaces its rounds with an unsupported summary and no
  preserved linked record, or leaves every full round duplicated in both the
  living design and final report.

PASS — closed-program evidence compaction:
  The living design keeps the final rolling summary, claim boundary,
  decision-changing findings, and links; a final report or append-only ledger
  preserves every complete round and artifact without duplication.

FAIL — formal but opaque:
  “Under PR7, optimize L over admissible z; M1 realizes the inductive bias and
  R3 passes.” The labels, objective, mechanism, result, and allowed conclusion
  require prior project context even if equations and references are present.

PASS — first-reader clarity:
  The document says that nearby images are assumed to change only a bounded
  amount, defines the matching objective and constraint, explains each stage's
  Goal, How, and Why, reports the measured result, and states what that result
  does and does not support. Necessary labels are defined where they first appear.

PASS — evidence boundary:
  evaluator truth is physically separate and scores only frozen decisions.
```

Run the stage-aware checklist in
[research_loop_checklist.md](research_loop_checklist.md) before implementation
or delivery.
