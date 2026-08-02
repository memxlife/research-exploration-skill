# Research Viewer Contract

Use this reference only when a plot, dashboard, HTML report, or result browser
materially helps a reader inspect research evidence. Do not require a viewer
for design-only work or evidence that is clearer as text or a table.

## Plot Contract Before Plotting

For each proposed plot, write:

```text
question answered
data and checkpoint source
metric definition and unit
x-axis, y-axis, and legend meanings
expected pattern under the conjecture
important alternative or failure pattern
number or pattern that will support the conclusion
claim boundary
```

If the plot cannot answer a distinct question, remove it or keep it as a named
debug artifact.

## Reader-Facing Requirements

The viewer must identify:

```text
purpose
exact setup or link to the frozen experiment contract
conditions being compared
how to read each plot
observed result in numbers or explicit pattern
narrow conclusion
remaining uncertainty
```

Define visible technical terms before using them. Use literal condition and
metric names rather than run IDs or project nicknames. Put important numeric
values next to the plot rather than forcing visual estimation.

Each visible plot must state or make immediately available:

```text
title and question
metric and unit
axes and legend
observed result
allowed conclusion
what it does not prove, when material
```

Never combine different units on one axis unless the transformation itself is
being tested and explained. State every scaling or normalization.

## Bounded Render Audit

Use one bounded cycle:

```text
plot contract -> implementation -> rendered inspection -> concrete fixes -> final
```

Inspect the actual rendered artifact for:

- missing or clipped titles, labels, legends, or values;
- undefined metrics or units;
- hidden scaling;
- ambiguous condition names;
- console or interaction errors when applicable;
- conclusions broader than the visible evidence; and
- redundant or unexplained plots.

Fix concrete failures and stop when the contract passes. If the renderer or
browser cannot be inspected, say so; do not claim visual verification.

Persistent serving, screenshots, an audit file, or independent review are
optional artifacts chosen when the user needs a durable or high-risk viewer.
Do not install a service or invoke an independent agent merely because a plot
exists.

## Result

- **PASS:** every visible plot is self-contained, correctly rendered, and
  supports only its stated conclusion.
- **FAIL:** a reader needs source code or chat history, units are mixed or
  hidden, rendering is broken, or the conclusion exceeds the evidence.
- **NOT APPLICABLE:** no viewer materially helps the current deliverable.

## Forward Checks

```text
FAIL: A plot labeled “score vs k” has no metric definition, unit, condition
      names, important values, or allowed conclusion.

PASS: The plot defines the measured probability, axes, conditions, key values,
      narrow conclusion, and the alternative it cannot rule out.

NOT APPLICABLE: A document-only mathematical design has no experiment result
      and therefore creates no viewer.
```
