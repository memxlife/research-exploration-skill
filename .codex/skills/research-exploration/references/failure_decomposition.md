# Failure Decomposition

Use this reference when a result is wrong but the cause is not yet local.

## Rule

Do not ask only "why did the whole system fail?" Break the failure into smaller
questions until the bottleneck is observable and fixable.

Use this structure:

```text
big failure -> sub-problems -> stage-local tests -> verified bottleneck -> targeted fix
```

## Record Each Level

For each decomposition level, record:

```text
parent failure
candidate sub-problems
test for each sub-problem
answer for each sub-problem
evidence supporting each answer
remaining bottleneck
```

Each level must produce an answer, even if the answer is "not the cause."
Negative answers are progress because they remove false explanations.

## Example Questions

Choose questions that match the domain. Common checks include:

```text
Is the visualization wrong?
Is the benchmark unable to answer the question?
Is the ground truth wrong or mismatched?
Are candidates missing?
Is the correct match outside the search region?
Is the evidence ambiguous?
Is the model rejecting correct cases?
Is the final decision too permissive?
Is the metric rewarding the wrong behavior?
```

Only change the algorithm after the decomposition identifies a specific failed
sub-problem. If multiple sub-problems remain plausible, instrument them first.

## Final Causal Path

When the issue is resolved, record:

```text
big failure -> falsified explanations -> verified bottleneck -> fix -> remaining unsolved problem
```
