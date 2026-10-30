# Incremental parallel resistance

Use this topic when a fixed bank of positive resistances undergoes
repeated changes at known indices and the equivalent resistance is needed
after each change. The useful representation is conductance, together
with a maintained sum. The [code](parallel_resistance.py),
[tests](test_parallel_resistance.py), [workload](run_workload.py),
[references](references.md) and results are kept together here.

## From the situation to the calculation

For ideal positive resistances in parallel,

$$G_i=\frac{1}{R_i},\qquad
S=\sum_i G_i,\qquad R_{\mathrm{eq}}=\frac{1}{S}.$$

Resistance is measured in ohms and conductance in siemens. If a
dimensionless transport is wanted, choose `R0>0`, put `r=R/R0` and use
`phi(r)=1/r`. Transporting positive addition gives

$$r_1\oplus r_2
=\frac{1}{1/r_1+1/r_2}
=\frac{r_1r_2}{r_1+r_2}.$$

This is a reciprocal transport restricted to positives. It is not a
generator defined on all real numbers or a complete Alpha field. In the
positive finite domain there is no additive identity. An open circuit
would add an infinite-resistance identity in a different, extended
physical domain; this implementation excludes infinities.

1. Validate a nonempty collection of positive finite resistances.
2. Convert each resistance to conductance and sum the conductances once.
3. For a change at known index `j`, calculate the new conductance and
   `S_new=S_old-G_old+G_new`.
4. Return `1/S_new` and the update trace.
5. Reconstruct explicitly if the numerical range or an application's
   accuracy requirements make the cached state unsuitable.

The two-branch example `[6, 3]` ohms has conductances `[1/6, 1/3]` siemens,
sum `0.5` siemens and equivalent resistance `2` ohms. Replacing the first
branch by `3` ohms gives `S=2/3` siemens and `R_eq=1.5` ohms. The test
`test_trace_matches_two_known_parallel_resistors` checks each intermediate.

## Run the scripts

From the repository root:

```sh
python3 -B topics/parallel_resistance/test_parallel_resistance.py
python3 -B topics/parallel_resistance/run_workload.py
```

The workload writes [its results](results/workload-results.json) beside
this topic, independently of the current working directory. The code uses
the Python standard library.

`ParallelResistanceBank` accepts Python `int`/`float` values, excluding
`bool`. All reciprocal values, totals and recovered resistances must fit
the positive finite floating-point range. The constructor documents these
requirements. `replace()` requires an integer index in `[0,n)`; validation
or numerical failure preserves the existing state. `snapshot()` returns
an immutable copy with an explicit `O(n)` cost.

## Cost, comparison and numerical limits

| Method | Construction | Known-index change and query | Total for `k` changes | Memory |
| --- | --- | --- | --- | --- |
| Recompute all conductances after every change | `O(n)` validation | `O(n)` | `O(n+kn)` | `O(n)` |
| Maintain conductance sum | `O(n)` | `O(1)` | `O(n+k)` | `O(n)` |
| Competent conventional conductance cache | `O(n)` | `O(1)` | `O(n+k)` | `O(n)` |

The cost model uses fixed-size floating-point arithmetic. Index search,
topology changes and explicit reconstruction are outside the constant-time
update. The improvement over recomputation comes from persistent state;
the conventional cache achieves the same asymptotic cost. Alpha's value
here is a systematic route to the representation and its explanation.

Cached totals are approximate. With `[1e-20, 1]` ohms, the smaller
conductance can be lost when the total is rounded. Replacing the dominant
branch then exposes cancellation. The helper rejects a sufficiently
cancellation-sensitive update before mutation. Its guard compares the new
total with the terms' scale using `sqrt(epsilon)`; this is a conservative
policy rather than a proved general error bound. Long update sequences can
still drift. Explicit reconstruction costs `O(n)` and is never hidden in
the advertised constant-time path.

## Executed evidence and scope

The eight tests cover 2000 deterministic updates against fresh `math.fsum`
recomputation, known traces, invalid domains and indices, overflow,
cancellation, single-branch replacement and preservation of state on error.

The workload runs 256 further changes for each of `n=8,128,2048`, with
resistances in `[10,1000]` ohms and seed `20261029+n`. It observes actual
helper calls and the lengths of `math.fsum` inputs. Each update sums three
terms; counts are work indicators, not elapsed times or machine-instruction
counts. Results and source hashes are in the
[execution record](results/verification.json). Successful bounded workloads
do not certify arbitrary floats or all update sequences.

The helper does not solve arbitrary circuit topologies, complex impedances,
tolerances or changing bank sizes. For one evaluation without subsequent
changes, both methods require `O(n)` work.
