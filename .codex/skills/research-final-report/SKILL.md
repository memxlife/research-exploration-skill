---
name: research-final-report
description: Create the final paper-style report for a research subproblem after it reaches a stable conclusion. Use automatically when a research subproblem has enough design, experiment, profiling, visualization, and analysis evidence to summarize the whole story end to end; use when the user asks for a final article, final report, paper-style writeup, final synthesis, or to put an end to a research story.
---

# Research Final Report

Use this skill to turn a solved or mostly settled research subproblem into a
self-contained research-paper-style report.

This skill is not for daily experiment notes. It is used after the working
documents have converged enough that a careful reader can learn the whole
subproblem without reading the chat history, raw code, raw logs, or every
intermediate document.

## Automatic Trigger

When a research subproblem reaches a stable conclusion, automatically create:

```text
docs/final_report.md
```

Do this even if the user does not explicitly ask for a final report. The final
report does not replace the working documents. It synthesizes them.

A subproblem has reached a stable conclusion when all of these are true:

```text
the main conjecture is stated clearly
the claim boundary is known
the main experiments have been run
the important plots or tables have been interpreted
major contradictions have either been resolved or written as limitations
the next question is different enough to become a new subproblem
```

If any of these are missing, do not write a final report yet. Say which missing
piece prevents final synthesis.

## Required Inputs

Before writing the final report, inspect the subproblem artifacts that exist:

```text
docs/design.md
docs/experiment_design.md
docs/visualization_results.md
docs/result_analysis.md, if present
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
Why this subproblem matters and what confusion it tries to resolve.

## 2. Problem Formulation
Objects, variables, model setting, and the exact question.

## 3. Physical Priors
Plain-language assumptions about the mechanism being tested.

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

## 10. Conclusion
Summarize the final answer in simple language.

## 11. Next Research Question
State the next question opened by the result and why it is separate.

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
the next research question is clearly separated from the solved subproblem
the appendix contains enough paths or commands to reproduce the evidence
```

If the report fails any item, revise it before presenting it.
