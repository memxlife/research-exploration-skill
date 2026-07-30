---
name: research-final-report
description: Create the final paper-style report for a research question after it reaches a stable conclusion. Use automatically when an active research question has enough design, experiment, profiling, visualization, and analysis evidence to summarize its bounded answer end to end; use when the user asks for a final article, final report, paper-style writeup, final synthesis, or to close one node in a research-question hierarchy.
---

# Research Final Report

Use this skill to turn a solved or mostly settled research question into a
self-contained research-paper-style report.

This skill is not for daily experiment notes. It is used after the working
documents have converged enough that a careful reader can learn the whole
question without reading the chat history, raw code, raw logs, or every
intermediate document.

## Automatic Trigger

Determine the current question's `node-dir` from `docs/research_map.md` when it
exists. For a single root question without a map, use `docs/`. When the question
reaches a stable conclusion, automatically create:

```text
<node-dir>/final_report.md
```

Do this even if the user does not explicitly ask for a final report. The final
report does not replace the working documents. It synthesizes them.

A research question has reached a stable conclusion when all of these are true:

```text
the main conjecture is stated clearly
the claim boundary is known
the main experiments have been run
the important plots or tables have been interpreted
major contradictions have either been resolved or written as limitations
the bounded answer can be returned to its parent, when a parent exists
any remaining question is a separate hierarchy node, or none (terminal)
```

If any of these are missing, do not write a final report yet. Say which missing
piece prevents final synthesis.

## Required Inputs

Before writing the final report, inspect the question artifacts that exist:

```text
<node-dir>/design.md
<node-dir>/experiment_design.md
<node-dir>/visualization_results.md
<node-dir>/result_analysis.md, if present
docs/research_map.md and any linked coupled-set contract, when present
shared experiment and result paths named by that coupled-set contract
viewer files or generated result summaries, if they contain conclusions
experiment scripts and result JSON/CSV files, when needed to verify a number
```

Use the working documents as evidence, but rewrite the story from scratch. Do
not paste a collection of old sections together if that makes the report hard
to read.

## Writing Standard

Write for a careful undergraduate student who knows linear algebra, probability,
and basic machine learning, but has not seen the project conversation.

The report must be rigorous and patient:

```text
define every important term before using it
state every variable in each equation
explain why an equation matches the physical prior
explain how the equation becomes code or a metric
explain what each experiment was expected to show
show what actually happened
separate evidence, interpretation, conjecture, and speculation
state what the result does not prove
```

Do not use buzzwords, unexplained abbreviations, or private project nicknames.
Use plain labels such as `standard cross-entropy`, `label smoothing`, `rare
feature`, `common feature`, `singular vector rank`, and `validation loss`.

All equations must use Markdown LaTeX:

```text
inline: \(z = Wx\)
block:
\[
L = -\log p_y
\]
```

Never leave raw bracket notation such as `[ W \approx ... ]` unless it is inside
a code block intentionally.

## Required Structure

Use this structure unless the user requests a different paper format:

```text
# Title

## Abstract
One paragraph stating the question, method, main finding, and limitation.

## 1. Motivation
Why this research question matters and what confusion it tries to resolve.

## 2. Problem Formulation
The exact research question, scope, parent, child, dependency, and coupling
relations, objects, variables, model setting, and current bounded answer.

## 3. Physical Priors
Plain-language conjectures about the structure of the world or workload.

## 4. Mathematical Model
Equations that formalize the priors. Define every symbol.

## 5. Computational Implementation
How the model, data, loss, metrics, and profiling were implemented.

## 6. Experimental Design
Datasets, model architecture, losses, training schedule, conditions compared,
metrics, expected outcomes, and falsification criteria.

## 7. Results
Each result gets its own subsection with setup, observed values or patterns,
and the narrow conclusion allowed by the evidence.

## 8. Analysis
Connect the results back to the mathematical model. Explain why the evidence
supports, weakens, or refines the conjecture.

## 9. Claim Boundary And Limitations
State exactly where the conclusion applies and where it should not be assumed.
If evidence is joint across a coupled set, state what answer is supported for
each member and what remains non-identifiable independently.

## 10. Conclusion
Summarize the final answer in simple language.

## 11. Next Research Question
State the next question opened by the result and why it is separate. If there
is no justified next question, record `none (terminal)` rather than inventing one.

## Reproducibility Appendix
List scripts, result files, viewer URL or path, important commands, seeds,
training steps, and output artifacts.
```

## Result Section Contract

Every important result section must contain:

```text
Purpose:
  what question this result answers

Setup:
  data, model, condition, metric, and what changed between compared runs

Expected if the conjecture is true:
  concrete pattern or numeric direction

Expected if the conjecture is false:
  concrete pattern or numeric direction

Observed result:
  numbers, plot references, or summarized patterns

Interpretation:
  why those observations matter

Take-home conclusion:
  one plain sentence a student should remember

What this does not prove:
  the most important limitation
```

If a plot exists, cite it by viewer section or file path and explain it in text.
Do not assume the reader can infer the conclusion from the plot.

## Claim Discipline

Use cautious scientific language:

```text
Supported:
  The experiment supports this mechanism in this benchmark.

Not supported:
  The experiment proves the mechanism in all transformers.
```

When using causal language, identify the intervention or falsification evidence.
If the evidence is correlational, say it is correlational.

If the report proposes a mechanism, include at least one possible alternative
explanation unless the experiments already rule it out.

## Final Quality Check

Before finishing the report, verify:

```text
the report can be read without the chat history
all equations render as LaTeX
all conditions and metrics are defined before results use them
each result has a setup and a take-home conclusion
the conclusion does not overclaim beyond the experiments
the next research question is clearly separated, or recorded as none (terminal)
the bounded answer and claim boundary can be propagated to the parent
joint evidence is not reported as an independently identified conclusion
every coupled member receives a bounded answer or explicit unresolved state
the appendix contains enough paths or commands to reproduce the evidence
```

If the report fails any item, revise it before presenting it.
