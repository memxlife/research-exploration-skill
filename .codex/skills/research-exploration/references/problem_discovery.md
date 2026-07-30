# Problem Discovery Before Optimization

Use this worksheet before selecting an open-ended research or optimization
mechanism.

## Contents

1. State the research question
2. Establish importance
3. Discover the problem structure
4. Derive, do not attach, the mechanism
5. Separate four failures
6. Apply the readiness gate

## State the research question

Write the open question that must be answered before proposing a solution. The
question may name a target object or capability, such as extracting a
transformation or constructing physically grounded features. It must not select
the solver, architecture, representation, loss, implementation, dataset, or
numeric target unless the researcher supplied it as part of the question.

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
structure status: observed or conjectured
physical structure and scope:
current supporting evidence, if any:
mathematical representation:
mechanism that exploits it:
predicted benefit:
correctness obligation:
counterexample:
measurement that distinguishes the explanation:
```

Reject a mechanism when the physical-structure field is empty or merely
restates the mechanism. A conjectured structure is allowed when it is labeled
as conjectured and paired with a predicted consequence and falsifier.

Examples:

- Sparse local edits may justify immutable snapshots plus delta updates.
- A stable prompt prefix may justify prefix-state reuse.
- Bounded runtime choices may justify a small admission checker.
- Repeated independent tiles may justify induction only after the required
  independence relation is proved.

These are conditional implications, not universal recipes.

## Separate four failures

When a test fails, determine which statement failed:

1. **Research-question failure:** the objects, scope, or causal framing do not
   capture what must actually be understood.
2. **Importance failure:** the measured cost is too small to matter.
3. **Structure failure:** the assumed stability, sparsity, locality, or bound
   is absent.
4. **Mechanism failure:** the structure exists, but this implementation does
   not exploit it effectively.

Do not abandon a valid structural hypothesis because one mechanism failed.
Do not keep tuning a mechanism after the assumed structure has been falsified.

## Readiness gate

Implementation of a proposed solution or a mechanism-comparison experiment may
begin only when the research note states:

```text
the current research question;
why this problem is worth solving;
the decision the result will change;
the observed or conjectured structure;
the mathematical object representing that structure;
the mechanism-to-structure mapping;
the smallest falsifier;
what outcome means stop, revise, or continue.
```

If the structure itself is uncertain, run an observational or profiling test
instead of benchmarking a proposed optimization. Before that test, state the
research question, why the structure matters, the candidate structural
alternatives, and the measurement that could distinguish them; a solution
mechanism is not yet required.
