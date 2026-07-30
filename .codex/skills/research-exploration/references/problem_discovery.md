# Problem Discovery Before Optimization

Use this worksheet before selecting an open-ended research or optimization
mechanism.

## Establish importance

Write one concrete sentence for each item:

1. **Affected system or person:** Who experiences the limitation?
2. **Current failure or cost:** What is slow, expensive, unreliable, unsafe,
   inaccurate, or impossible today?
3. **Decision:** Which design, scientific, or operational decision would a
   solution change?
4. **Counterfactual:** What happens if the problem is left unsolved?
5. **Success consequence:** What becomes possible if it is solved?
6. **Boundary:** At what scale or frequency does the problem become too small
   to justify further work?

Do not use “important,” “scalable,” or “efficient” without naming the measured
object and consequence.

## Discover the problem structure

Describe the system before proposing a mechanism.

| Question | Examples of consequential structure |
|---|---|
| What remains stable? | document body, topology, specification, weights |
| What changes? | local edit, request, schedule, load, failure state |
| What is local and what is global? | selected passage versus distant invariant |
| What is sparse or repetitive? | small patches, repeated tiles, recurring queries |
| What is bounded? | shape family, resource capacity, action set, error budget |
| When does information become known? | design, compile, launch, runtime |
| What is authoritative? | exact source, accepted decision, measurement |
| What is advisory? | summary, prediction, generated proposal |
| What is expensive to get wrong? | chip respin, stale edit, unsafe policy |
| What dominates cost? | uncached prefill, memory traffic, synchronization |

A “physical prior” is a causal property of the actual workload or system. A
domain label such as tensor, dataflow, agentic, or interactive is not itself a
prior.

## Derive, do not attach, the mechanism

For every proposed mechanism, complete this record:

```text
observed structure:
mathematical representation:
mechanism that exploits it:
predicted benefit:
correctness obligation:
counterexample:
measurement that distinguishes the explanation:
```

Reject a mechanism when the “observed structure” field is empty or merely
restates the mechanism.

Examples:

- Sparse local edits may justify immutable snapshots plus delta updates.
- A stable prompt prefix may justify prefix-state reuse.
- Bounded runtime choices may justify a small admission checker.
- Repeated independent tiles may justify induction only after the required
  independence relation is proved.

These are conditional implications, not universal recipes.

## Separate three failures

When a test fails, determine which statement failed:

1. **Importance failure:** the measured cost is too small to matter.
2. **Structure failure:** the assumed stability, sparsity, locality, or bound
   is absent.
3. **Mechanism failure:** the structure exists, but this implementation does
   not exploit it effectively.

Do not abandon a valid structural hypothesis because one mechanism failed.
Do not keep tuning a mechanism after the assumed structure has been falsified.

## Readiness gate

Implementation or experimentation may begin only when the research note states:

```text
why this problem is worth solving;
the decision the result will change;
the observed or conjectured structure;
the mathematical object representing that structure;
the mechanism-to-structure mapping;
the smallest falsifier;
what outcome means stop, revise, or continue.
```

If the structure itself is uncertain, the next experiment should measure the
structure rather than benchmark a proposed optimization.
