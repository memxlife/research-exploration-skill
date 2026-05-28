# Goal Audit

Use this reference when repeated reasonable fixes fail or when the old metric no
longer matches the real purpose of the work.

A goal audit is not giving up. It is part of research. Sometimes the failed
iterations show that the old goal was too strict, too loose, or pointed at the
wrong downstream need.

## Trigger

Do not only keep changing the algorithm. Audit the goal when:

```text
several reasonable operationalizations fail
the same error pattern keeps returning
the label may not match the downstream purpose
false positives and false negatives have different costs
a high metric still produces an unhelpful result
```

## Questions

Ask:

```text
What is the downstream task?
What decision will use this result?
Are we solving that decision, or only matching a convenient label?
Are the labels too strict, too loose, or mismatched?
Do false positives and false negatives have equal cost?
Which old errors are actually acceptable or useful?
Which old errors are still harmful?
Would another metric better capture useful progress?
What is costly to miss?
What is safe to include even if it is not perfectly labeled?
```

## Record

Write the goal audit in simple terms:

```text
original goal
downstream purpose
old success metric
observed failure pattern
cost of false positives
cost of false negatives
revised goal
revised metric
which old errors become acceptable or useful
which old errors remain harmful
```

This matters because a "false positive" under the old label may be useful for
the real downstream task, and a high-scoring metric may still optimize the wrong
thing.

## After The Audit

If the goal changes, update the current-state document first. Then design the
next experiment against the revised goal.
