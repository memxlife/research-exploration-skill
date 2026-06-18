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

This is a hard gate. A plot that is not self-explanatory must not be shown in
the main viewer. The agent must evaluate every plot before presenting it. If
the plot fails the evaluation, the agent must revise, split, relabel, annotate,
or remove the plot before showing the viewer to the user.

Do not assume the reader remembers the conversation, code names, file names,
internal variables, or previous experiment history. Every term visible in the
viewer must either be common language or defined before it is used.

Do not be brief at the cost of understanding. The viewer is part of the
profiling and falsification process, not a decorative chart gallery. It should
teach the reader what feedback the experiment gives. If a plot needs five
sentences to explain the purpose, setup, axis meaning, observed result, and
claim boundary, write the five sentences.

Never combine metrics with different units on one axis unless the transformation
is the object being tested. Do not hide scaling factors in code or legend text.
If one metric is an angle and another is a probability, percentage, loss, count,
or normalized score, use separate plots or separate axes with explicit units.
Separate plots are preferred.

Avoid buzzwords and compressed labels. Do not use terms such as "viral",
"phase", "magic", "diagnostic score", "bottleneck", "alignment", or "mass"
unless the page defines exactly how the quantity is computed and why it matters
for this experiment. Prefer literal names that describe the data-generating
process or computation.

## Build The Explanation Before The Plot

Do not create a chart first and then try to explain it afterward. For every
plot, write the visible explanation first. The plot should be the picture of
that explanation.

Use this order:

```text
1. Write the research question answered by this plot.
2. Write the exact data and checkpoint source.
3. Define the metric in plain language.
4. Define the formula and unit when useful.
5. Define the axis meaning and legend meaning.
6. State the expected pattern if the hypothesis is right.
7. State the expected pattern if the hypothesis is wrong or incomplete.
8. Only then draw the plot.
```

This prevents the common failure mode where the viewer contains a technically
correct chart but the reader cannot tell what it means.

## Bounded Verification, Not Endless Checking

Verification is required, but it should not become the main activity. The
research viewer workflow is:

```text
plot contract -> implementation -> one rendered audit -> concrete fixes -> final viewer
```

Do not repeatedly refresh, screenshot, and patch a viewer without changing the
plot contract. If a plot remains confusing after one audit, the likely problem
is the metric, title, axis, legend, or conclusion. Rewrite the plot contract,
split the plot, or remove the plot.

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

The overview must be long enough to make the page usable without the chat
history. One paragraph can be enough for a simple experiment. A multi-condition
research viewer often needs a table plus several paragraphs.

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

The text under a plot is part of the result. Do not compress it into a short
caption when the experiment is subtle. For important plots, use this full
teaching structure:

```text
Purpose:
  The specific question this plot answers.

Exact setup:
  Model, data, checkpoint, matrix, loss, probe set, and grouping used for this
  plot. Include values such as number of training steps, epsilon, bin size, or
  top-k cutoff when they matter.

Metric:
  Plain-language definition, formula if needed, unit, and direction of
  interpretation.

How to read:
  What x-axis, y-axis, line color, bar color, sign, or marker means.

Observed result:
  The main numbers or visual pattern. Do not force the reader to estimate the
  key comparison from the chart.

Take-home:
  The narrow conclusion supported by this plot.

What this does not prove:
  The most important limitation or alternative explanation.
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

## Stable Static Viewer Serving

Research viewers are often revisited across many turns. A viewer that works
only because a temporary terminal command is still alive is not reliable enough.

For static HTML viewers, prefer a persistent local server. The skill provides:

```text
scripts/ensure_static_viewer_server.sh
```

Use it like this:

```bash
bash .codex/skills/research-exploration/scripts/ensure_static_viewer_server.sh \
  --root /absolute/path/to/project \
  --port 4182 \
  --label com.representation-space.viewer
```

The script installs or refreshes a macOS LaunchAgent that serves the project
directory with `python3 -m http.server`, keeps the process alive, verifies that
the URL returns HTTP 200, and prints restart/check commands.

Record these in `docs/viewer_audit.md` or `docs/visualization_results.md`:

```text
viewer URL
server label
project root served
port
restart command
last HTTP status check
```

If a project cannot use a LaunchAgent, use `tmux` or a foreground process and
write the exact restart command in the final response. Do not leave the user
with only "try reload" as the recovery plan.

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

## Mandatory Pre-Publish Plot Audit

Before a plot is visible in the main viewer, write or mentally verify this
audit. If any answer is missing or confusing, the plot fails and must not be
shown.

```text
Plot title:
Question answered:
Metric definition:
Formula, if any:
Unit:
Data source:
Exact setup:
X-axis meaning:
Y-axis meaning:
Color/shape/legend meaning:
Whether larger is better, smaller is better, or neither:
Observed result in numbers:
Allowed conclusion:
What this plot does not prove:
Possible reader confusion:
Fix applied before showing:
```

The plot fails automatically if:

```text
two metrics with different units share one axis;
a metric is scaled or transformed but the title, axis label, and explanation do
  not state the transformation;
the legend is clipped, ambiguous, or uses internal names;
the metric name is not defined before the plot;
the reader must inspect code to know what was computed;
the conclusion depends on a number not visible in the plot or nearby text;
the plot looks technically correct but is hard to explain in one plain sentence.
```

When a viewer is updated after a user reports confusion, first fix the metric
definitions and plot audit failure, then regenerate the viewer. Do not defend
the old plot.

## Required Viewer Harness

Every viewer update must produce a harness record. Prefer:

```text
docs/viewer_audit.md
```

The audit must contain one entry per visible plot. Each entry must include:

```text
plot title
status: pass, fail, removed, or debug-only
metric definition
unit
axis check
legend check
unit compatibility check
visible-number check
reader-confusion risk
fix applied
allowed conclusion
remaining uncertainty
```

A plot cannot be marked `pass` if:

```text
metric definition is absent from the viewer;
unit is absent from the viewer;
two metrics with different units share the same axis;
the plot uses a hidden scaling factor;
the legend is clipped or ambiguous;
the plot needs source-code knowledge to understand;
the conclusion is broader than the plotted evidence;
important numeric values are only inferable by estimating from the chart.
```

For metrics that are new, abstract, or easy to misunderstand, the viewer must
show a metric definition block before any plot that uses the metric. The
definition block must include:

```text
plain-language meaning
formula, if useful
unit
whether higher or lower is better
one concrete example number
what the metric does not measure
```

If the viewer contains more than one plot, the agent must decide whether each
plot answers a different question. If two plots answer the same question, keep
the clearer plot and remove the other one.

## Independent Review Gate

When multi-agent or reviewer tools are available and the current tool policy
permits delegation, use an independent reviewer before delivering a research
viewer. The reviewer should inspect the rendered artifact as a fresh reader,
not the source code first.

Reviewer prompt:

```text
Read the rendered viewer as if you did not see the conversation.
For every visible plot, answer:
- What metric is shown?
- What is the unit?
- What does each axis mean?
- What does the legend mean?
- What number or pattern matters?
- What conclusion is allowed?
- What remains uncertain?
Flag any plot that is not self-explanatory.
```

If independent review is not used, record why in `docs/viewer_audit.md` and run
the same checklist manually.

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
