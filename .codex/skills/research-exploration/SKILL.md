---
name: research-exploration
description: Guide problem-first research exploration for ambiguous scientific, systems, ML, robotics, computer vision, or algorithm-design work. Use when Codex must form and explore research questions, conjecture physical structure, turn that structure into mathematical models and computation, design falsification and profiling experiments, inspect evidence, or recursively refine questions only when reasoning or evidence reveals smaller problems.
---

# Research Exploration

Use this skill to keep research work concrete, testable, and evidence-driven.

## Communication Rule

Use simple language. Be precise without using fancy words. Name the concrete
object, variable, file, metric, stage, example, or decision being discussed.
Do not use buzzwords, project nicknames, vague abstractions, or compressed
phrases when a concrete description is possible.

When explaining a result, say:

```text
what was tested
where the evidence is
what passed
what failed
why it failed, if known
what the next concrete test is
```

Do not use polished research language to hide an unclear idea. If a term is
important, define it as a test or computation.

For visualization and result analysis, do not try to save words. The purpose of
the viewer is to provide feedback that helps the researcher understand the
problem structure. Each result should explain enough context for a careful
undergraduate reader to understand what was measured, how to read it, what was
observed, and what conclusion is allowed.

## Result-First Rule

When the user asks for a concrete experimental result, number, accuracy, loss,
metric, status, or comparison, return the direct first-hand result as soon as it
is available. Do not delay the answer in order to polish the viewer, update a
document, reorganize files, or add extra analysis.

Research is an iterative exploration process. Fast turnaround is part of the
method, not a convenience. Prefer the shortest reliable measurement that can
answer the current question, report it immediately, and only then decide whether
larger experiments, cleaner plots, or deeper documents are worth the time.

For experiment questions, use this order:

```text
1. get the minimal measurement needed to answer the question
2. report the first-hand result immediately
3. then refine visualization, documents, interpretation, or follow-up analysis
```

If the result is already known from a completed command, JSON file, log, or
viewer artifact, answer with the number first. Then mention where the result
came from and whether a caveat matters. Only after that should you propose or
perform viewer/document cleanup.

Learning should have no barrier. When presenting experimental results, write
patiently. Do not assume the reader remembers the conversation, knows why a
metric matters, or can infer the lesson from a table. For each important result,
include the missing bridge between the number and the conclusion:

```text
what the model/data looked like in plain language
what the metric means before showing the value
what value would be expected if the hypothesis were true
what value would be expected if the hypothesis were false
the actual values
how to compare the values
the narrow conclusion from that comparison
what a student should remember
```

Avoid compressed phrases such as "confirms the mechanism" unless the mechanism
has just been restated in plain language. Prefer concrete sentences like:
"The rare example learned later because the common update pointed partly toward
the wrong answer." Do not use unexplained labels, abbreviations, or shorthand.
If a table has more than three columns of metrics, explain each metric before
the table and tell the reader which one to inspect first.

Do not rely on repeated post-hoc checking to rescue unclear visualization work.
The viewer should be designed from explicit plot contracts before code is
written. Verification is still required, but it must be bounded: render once,
inspect against the audit checklist, fix concrete failures, and stop when the
viewer satisfies the contract. Do not spend research time repeatedly refreshing
or manually checking a viewer whose plot definitions were never made clear.

## Problem-First Gate

Do not begin with a proposed model, optimizer, cache, language, architecture,
benchmark, or implementation. First establish:

1. **Research question:** state what must be understood or achieved without
   choosing a solution.
2. **Importance:** name the affected person or system, the present limitation
   or cost, the decision that a solution would change, and the consequence of
   leaving the problem unsolved.
3. **Candidate structure:** identify what may be stable or changing, local or
   global, sparse or dense, bounded or open, known early or known late,
   authoritative or advisory, and cheap or costly to get wrong.
4. **Mechanism mapping:** after forming a physical prior and mathematical model,
   state exactly which property each proposed mechanism exploits and why that
   property should improve the target outcome.

If importance is weak, narrow or stop the work. If the structure is unknown,
investigate it before optimizing. If a mechanism cannot be mapped to a named
property, treat it as premature.

This gate applies to open-ended research, design, and optimization. Do not
burden a routine deterministic operation—such as formatting a file or running
an already specified command—with a new research justification.

Read [references/problem_discovery.md](references/problem_discovery.md) when
the problem is new, the proposed mechanism arrived before the model, several
optimizations appear plausible, or an experiment produced a result that does
not answer the user's real question.

## Recursive Research-Question Refinement

Treat the research state as an evolving hierarchy whose center is the
**current research question**. Keep every active research unit in exactly four
parts:

```text
1. Problem Definition
2. Physical Priors
3. Mathematical Model
4. Computational Implementation
```

Research-question refinement is not a fifth part. It is a possible
evidence-driven transition between recursive four-part units.

In `Problem Definition`, state the current research question first, then its
importance and scope, parent question, child questions and relations, current
bounded answer, and active frontier. A child must be a research question. It
may name a target object or capability, such as extracting a transformation or
constructing invariant features, but it must not prematurely choose the solver,
architecture, loss, implementation, dataset, or numeric threshold. Do not
silently add these to the question when the researcher did not specify them.
For every child, record whether it came from the researcher, initial causal
reasoning, or experimental evidence; `children: none (current leaf)` is valid.

In `Physical Priors`, state the conjectured structure of the world or workload.
Make each prior falsifiable by stating the observable consequence expected if
it holds. Then derive the mathematical model and computational implementation
used to falsify and profile that conjecture.

Use researcher input, explicit causal reasoning, or evidence to decide whether
to refine the question hierarchy. Do not invent a large tree upfront. When one
child or a coupled set becomes active, give each question its own recursive
four-part unit and name any shared prior, model, or experiment. Preserve
refinement, dependency, and coupling relations, and propagate bounded answers
through every affected edge.

Read [references/problem_refinement.md](references/problem_refinement.md) when
creating or revising a question hierarchy, choosing the active frontier, or
turning profiling evidence into smaller research questions.

## Core Rule

Do not treat a plausible idea as progress. Use this research loop:

```text
research question -> physical-structure conjecture -> mathematical model
-> computational implementation -> falsification + profiling -> evidence
-> refined understanding, question, or conjecture
```

The physical prior is the structural core of the conjecture. The full
falsifiable conjecture also states what observable consequence should follow
if that structure is real.

A failed experiment is useful only when it reveals which assumption, stage, or
prior was wrong. A successful experiment is useful only when it explains why the
result succeeded.

Repeated failure can also mean the goal is wrong. If several precise algorithms
fail in the same way, stop and ask whether the target label, metric, or success
condition matches the downstream purpose.

## Required Chain

For nontrivial research work, keep this chain inspectable:

```text
current research question -> conjectured physical structure
-> predicted observable consequence -> mathematical model
-> computational implementation -> falsification + profiling
-> evidence -> refined question, structure, model, or implementation
```

Show how each prior becomes a model, how each model becomes code, and how
profiling evidence improves understanding of the problem structure. Evidence
may answer or reframe the current question, create child questions, change
relations among existing questions, or update an ancestor. Keep history in the
iteration ledger rather than hiding it in the current design.

## Required Artifacts

Do not deliver a final research answer unless the notes, report, or response
contain:

```text
current research question, importance, scope, and current bounded answer
parent question and required upward answer
child research questions with refinement source, or an explicit current-leaf state
typed relations and active frontier or an explicit answered/blocked state
physical priors and predicted observable consequences
relations among independent, dependent, coupled, or competing priors
joint contract for every coupled question or prior set
explicit mapping from each mechanism to the physical structure it exploits
mathematical model for each prior or coupled set of priors
implementation contract for each model
publication-grade experimental setup
explicit algorithm specification for each nontrivial stage
stage-level profiling evidence
failure interpretation for each stage
question, hierarchy, or conjecture update
claim boundary
```

If an artifact is missing, say the research state is incomplete and name the
missing artifact.

When a self-contained research question reaches a stable conclusion,
automatically use the sibling `research-final-report` skill to create its
`final_report.md`. This final report is required before treating the node as
closed. It is a synthesis article, not another experiment log.

## Research-Question Document Standard

For a single research question, use `docs/` as `node-dir`. When refinement
creates multiple retained questions, add `docs/research_map.md`, assign stable
IDs such as `P0` and `P0.1`, and use `docs/problems/<ID>/` for each newly active
node. Map any existing root documents to `P0`; do not duplicate them only to
change layout. In a multi-question program, `docs/research_map.md` is
authoritative for graph relations and the program active frontier. Each node
design is authoritative for that node's question, priors, models, bounded
answer, and local frontier.

For each active research question, maintain exactly these three primary
working documents unless the user requests a different structure:

```text
<node-dir>/design.md
  1. Problem Definition
     1.1 Current research question
     1.2 Importance and scope
     1.3 Parent question and upward-answer contract
     1.4 Child research questions and typed relations
     1.5 Current bounded answer and claim boundary
     1.6 Local frontier or explicit answered/blocked state
  2. Physical Priors
  3. Mathematical Model
  4. Computational Implementation

<node-dir>/experiment_design.md
  detailed falsification and profiling plan, including pass/fail/insufficient
  evidence conditions

<node-dir>/visualization_results.md
  problem-specific viewer description, actual experiment results, how to read
  each result, observed result, take-home conclusion, and remaining uncertainty
```

Also keep the append-only research history in `<node-dir>/iterations.md`. It is
an auxiliary ledger, not a fourth current-state document.

After the research question reaches a stable conclusion, create a fourth synthesis
document:

```text
<node-dir>/final_report.md
  final paper-style report that merges problem formulation, physical priors,
  mathematical modeling, computational implementation, experiment design,
  results, analysis, claim boundary, conclusion, and next research question
```

Use `final_report.md` only after the working documents and evidence are
stable enough to tell the whole story end to end. It should be rigorous,
student-readable, and self-contained. A new reader should not need the chat
history, raw logs, or private context to understand the research question.

The visualization/results document is not a screenshot dump. It must explain
what each plot proves, what it does not prove, and how the viewer supports the
current claim boundary.

Every research report and viewer must include a dedicated experimental setup
section before the result plots. This section should read like the experiment
setup section of a research paper, not like a short caption. It must define the
objects being compared before any result label uses them.

The setup section must include, when applicable:

```text
research question
dataset construction or data-generating process
train/validation/test split or probe set
model architecture
input representation and position encoding
loss function
optimizer or update rule
training steps, tokens, batch size, and checkpoint interval
random seed and deterministic/stochastic choice
all conditions being compared, with plain-language labels
which variables are changed between conditions
which variables are held fixed
metric definitions, units, and thresholds
script path and output artifact path
known limitations of the setup
```

If a condition name appears in a plot or table, it must be defined in the setup
section before the plot. Labels like "orthogonal conflict" or "strong overlap"
are not self-explanatory unless the page states the exact values and plain
meaning.

The same standard applies to the viewer itself. Every visible plot should carry
its own explanation. A plot caption that only says "higher is better" is not
enough. State the exact comparison, the metric definition, the axis meaning, the
observed numbers or pattern, and the take-home conclusion. If the plot cannot be
explained clearly, remove it from the main viewer.

## Quick Workflow

1. State the current research question and why answering it matters.
2. Locate it relative to known parent, child, dependency, and coupling relations.
3. Conjecture the physical structure that may make an answer possible.
4. State the observable consequence expected if that structure holds.
5. Derive the mathematical model, then the computational implementation.
6. Define success, failure, invalid-test, and insufficient-evidence outcomes.
7. Run the smallest useful falsification and expose stage-level profiling.
8. Report the direct result, then classify what the evidence changes.
9. Refine the question hierarchy only where the evidence reveals a smaller question.
10. Propagate bounded answers through affected relations and select the next frontier.
11. Update the current-state document and iteration ledger.
12. When a question reaches a stable conclusion, use `research-final-report`
    to create its `final_report.md`.

## Non-Negotiable Rules

Do not run an experiment against a hand-waved algorithm. For any nontrivial
algorithm, first write:

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

Do not confuse a research question with a mechanism. “How can a shared spatial
transformation be extracted?” is a research question. “Use Kabsch with RANSAC”
is a proposed mechanism. Preserve the open question until physical priors and a
mathematical model justify a particular mechanism.

Do not silently turn qualitative language in a research question into an
arbitrary number. If “substantially more data-efficient” must become a threshold
for one experiment, record the chosen value and rationale as an operational
definition. Keep the broader research question unchanged.

Do not debug only the final output of a pipeline. Each stage must expose enough
evidence to explain why examples pass, fail, or become uncertain before the next
stage consumes them.

Do not stop at a yes/no outcome. The "why" comes from stage-level profiling:

```text
stage -> artifact -> pass/fail criteria -> representative examples -> next-stage handoff
```

When an experiment fails, say whether it falsified the physical prior itself or
only one operationalization of that prior.

When observations unfold over time or changing conditions, do not replace that
with a single-observation proxy unless the proxy itself is being tested.

For slow research loops, run a fast micro-test first. Use known good and bad
examples, a small number of observations or cases, and stage-local artifacts.

## Non-Negotiable Viewer Harness

Before creating or revising a research viewer, read
[references/research_viewer_design.md](references/research_viewer_design.md)
and use its complete plot contract and audit.

Every visible plot must let a new reader identify the question, data, metric
formula and unit, axes and legend, observed result, allowed conclusion, and
important limitation without reading code or chat history. Revise, split,
relabel, or remove any plot that fails. Never combine different units on one
axis without an explicit transformation that is itself being tested.

Use all five gates:

```text
Gate 1: Plot contract before plotting
Gate 2: Self-explanatory viewer implementation
Gate 3: Bounded rendered artifact audit after plotting
Gate 4: Stable local serving for browser-based viewers
Gate 5: Independent review before delivery, when delegation tools are available
  and tool policy permits their use
```

Record the audit in `<node-dir>/viewer_audit.md`. In the final response, name the
audit, review method, important plot or metric changes, supported conclusion,
and remaining uncertainty.

## Reference Files

Load only the reference file needed for the task:

- `references/algorithm_specification.md`: when an algorithm has multiple steps, thresholds, matching, clustering, fitting, ranking, or hidden heuristics.
- `references/profiling_and_evidence.md`: when planning experiments, running tests, reviewing results, or deciding what evidence is missing.
- `references/failure_decomposition.md`: when a failure is broad, confusing, or could have several causes.
- `references/goal_audit.md`: when several reasonable fixes fail, when labels may not match the downstream purpose, or when false positives and false negatives have different costs.
- `references/research_documentation.md`: when writing or revising a research document, design note, experiment note, or iteration ledger.
- `references/research_viewer_design.md`: when creating or revising an experiment visualization viewer, dashboard, HTML report, or plot set.
- `references/research_loop_checklist.md`: when a short checklist is enough for planning or review.
- `references/problem_discovery.md`: when establishing importance, discovering
  exploitable structure, or deriving a mechanism from that structure.
- `references/problem_refinement.md`: when managing current, parent, and child
  research questions or propagating evidence through the refinement hierarchy.
- `references/latex_toolchain.md`: when building or auditing a LaTeX paper.

## Writing Standard

Use concise causal structure:

```text
Objective and conclusion
1. Problem Definition
2. Physical Priors
3. Mathematical Model
4. Computational Implementation and Results
```

Every equation must map to a physical prior and a code path. Every
hyperparameter must have a name, value, definition, reason for the value, and
expected effect when it is too low or too high when that effect matters.

Write simply. Rigor means precise, not fancy. A reader should be able to
implement the algorithm from the document without guessing.
