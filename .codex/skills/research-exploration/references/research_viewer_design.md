# Research Viewer Design

Use this reference when creating or revising an experiment visualization viewer,
dashboard, static HTML report, plot page, or result browser for research work.

The viewer is not decoration. It is the evidence surface for understanding the
problem structure. A reader should learn:

1. what question the experiment asks;
2. what was exactly tested;
3. what each plot measures;
4. what result was observed;
5. what conclusion is allowed;
6. what uncertainty remains.

## Main Rule

Every viewer must be self-explanatory to a careful undergraduate reader.

Do not assume the reader remembers the conversation, code names, file names,
internal variables, or previous experiment history. Every term visible in the
viewer must either be common language or defined before it is used.

Do not be brief at the cost of understanding. The viewer is part of the
profiling and falsification process, not a decorative chart gallery. It should
teach the reader what feedback the experiment gives. If a plot needs five
sentences to explain the purpose, setup, axis meaning, observed result, and
claim boundary, write the five sentences.

Avoid buzzwords and compressed labels. Do not use terms such as "viral",
"phase", "magic", "diagnostic score", "bottleneck", "alignment", or "mass"
unless the page defines exactly how the quantity is computed and why it matters
for this experiment. Prefer literal names that describe the data-generating
process or computation.

## Required Page Structure

Every experiment viewer must start with an overview section containing these
blocks:

```text
Purpose
Exact setup
What is being compared
How to read the plots
Key observations
Current conclusion
Remaining uncertainty
```

### Purpose

State the scientific question in one plain sentence.

Good:

```text
Purpose: test whether label smoothing learns injected rare facts while keeping
the strongest output-head direction smaller than standard CE.
```

Bad:

```text
Purpose: analyze viral LS attribution.
```

### Exact Setup

List concrete experimental settings:

```text
model architecture
training dataset
continued-training dataset
loss function
number of training steps or tokens
probe set
matrix being analyzed
metric definitions
checkpoint source
```

Do not hide important setup in scripts or file names. The viewer must describe
the setup in visible text.

### What Is Being Compared

If the experiment compares conditions, use a small table. Use plain condition
names.

Good condition names:

```text
base CE
base label smoothing
rare-fact continued CE
rare-fact continued label smoothing
```

Bad condition names:

```text
viral CE
phase2 ls
run3
condition B
```

Internal result keys may remain in JSON, but visible labels must be human
readable.

## Required Plot Structure

Every plot must have these visible fields:

```text
Title
Purpose
Setup
How to read
Observed result
Take-home
Remaining uncertainty, when the result is not enough to settle the question
```

Use this template:

```html
<section>
  <h2>Plain plot title</h2>
  <p>One or more clear sentences explaining what question this plot answers.</p>
  <div class="explain">
    <div>
      <strong>Purpose</strong>
      <p>What problem this plot is meant to resolve.</p>
    </div>
    <div>
      <strong>Setup</strong>
      <p>What data and computation produced this plot.</p>
    </div>
    <div>
      <strong>How to read</strong>
      <p>What x-axis, y-axis, color, sign, or bar height means.</p>
    </div>
    <div>
      <strong>Observed result</strong>
      <p>The concrete numerical or qualitative observation.</p>
    </div>
    <div>
      <strong>Take-home</strong>
      <p>The narrow conclusion this plot supports.</p>
    </div>
    <div>
      <strong>Remaining uncertainty</strong>
      <p>What this plot does not prove, if anything important remains open.</p>
    </div>
  </div>
</section>
```

If a plot cannot support a clear take-home, remove it from the main viewer or
move it to an appendix/debug section.

For comparison plots, the take-home must focus on the comparison. For example,
a validation-loss plot should compare validation loss across methods; it should
not jump directly to a spectral conclusion. Put the spectral conclusion on the
spectral plot.

## Naming Rules

Use names that explain the data-generating process.

Avoid:

```text
viral
phase2
sigma magic
H_i
S_i
rank-grid
condition A/B/C
bottleneck score
alignment metric
mass curve
```

Prefer:

```text
injected rare facts
rare-fact continued training
largest output-head direction
loss change after removing one direction
loss sensitivity to one direction
number of singular directions included
validation CE
validation token accuracy
mean singular value in rank bin
```

Mathematical symbols are allowed only after the plain-language meaning appears.

Good:

```text
Loss change after removing one direction. Positive means the direction was
hurting this token. We denote this score by H_i.
```

Bad:

```text
H_i remove
```

## Plot Inclusion Rules

Include a plot only if it directly answers one of the experiment questions.

Remove or hide a plot when:

```text
the reader cannot interpret it without reading code;
the plot has no setup or conclusion;
the term names are internal implementation names;
the result is redundant with a clearer plot;
the plot only exists because the data was easy to draw;
the conclusion is "unclear" and no failure analysis is attached.
```

For exploratory work, put unclear plots under an appendix titled:

```text
Debug plots not used for the current conclusion
```

## Axis and Legend Rules

Axes must describe what is measured, not only the variable name.

Good:

```text
x-axis: number of strongest output-head directions included
y-axis: correct-token probability
```

Bad:

```text
x-axis: k
y-axis: p
y-axis: mass
y-axis: score
```

Legends must use the same condition names as the overview table. Do not mix
internal keys and human labels.

## Required Teaching Text

For each plot, add one sentence starting with:

```text
Read this plot as:
```

Example:

```text
Read this plot as: if the curve becomes good only after many directions are
included, the selected token needs a broad output subspace.
```

Also add one sentence starting with:

```text
This means:
```

Example:

```text
This means: label smoothing learned the rare fact while using a smaller largest
output-head direction.
```

When the plot is central to the argument, add one sentence starting with:

```text
What this does not prove:
```

Example:

```text
What this does not prove: this plot does not prove that rare features improved;
it only shows that validation loss is similar across methods.
```

## Quantitative Reporting

When possible, include the important numbers in text next to the plot:

```text
CE largest direction: 12.4
label smoothing largest direction: 6.1
CE target probability: 0.94
label smoothing target probability: 0.85
```

Do not force the reader to estimate key results from a chart.

## Error Prevention Checklist

Before finishing a viewer, check:

```text
no undefined code names are visible;
no buzzwords or project nicknames are used as visible terms;
no raw LaTeX appears in a non-math-rendered page;
each plot has purpose, setup, how-to-read, observation, take-home, and remaining
  uncertainty when needed;
all axis labels are plain language;
all legends use human-readable names;
every conclusion is supported by a visible number or plot;
each plot conclusion discusses the metric shown in that plot before drawing any
  cross-plot conclusion;
unclear plots are removed or moved to appendix;
the page loads without console errors;
interactive controls visibly change the selected result;
screenshots show the first screen and one selected interaction.
```

## Final Response After Viewer Work

When reporting viewer updates, state:

```text
what confusing terms were removed;
what plots were removed or kept;
what explanatory text was added;
what browser checks were run;
what conclusions the viewer now supports;
what remains uncertain.
```
