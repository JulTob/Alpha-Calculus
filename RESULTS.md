# Reproduced results

Both English notebooks were executed successfully with CPython
**3.14.3** on macOS arm64, each in a fresh process. All numerical
assertions passed.

| Standalone notebook | Total cells | Python cells | Execution record |
|---|---:|---:|---|
| Gain chains | 20 | 10 | [Execution](topics/gain_chains/results/execution.json) |
| Power laws and elasticity | 23 | 13 | [Execution](topics/power_laws/results/execution.json) |

Each application also has separate numerical-check and standalone
records:

- Gain chains: [numerical checks](topics/gain_chains/results/checks.json)
  and [standalone check](topics/gain_chains/results/standalone.json).
- Power laws and elasticity:
  [numerical checks](topics/power_laws/results/checks.json)
  and [standalone check](topics/power_laws/results/standalone.json).

An execution record identifies the runtime and the hash of its notebook
snapshot. A standalone record concerns a check with only that notebook
copied to an empty directory and its cells executed in a fresh process.
Saved outputs do not constitute a new execution by the reader.

Both standalone checks passed with CPython 3.14.3 in isolated mode
(`-I -B`). The generated CSV tables and numerical-check records were
identical to those produced by the main runner. The individual `gains`
and `power-laws` commands also passed with only the selected notebook
and the runner present. Each notebook's saved outputs come from the
English revision's CPython 3.14.3 execution.

After the topic migration, both standalone checks were repeated. Each
generated `example.py` also passed from an unrelated working directory
and when copied on its own. Its numerical CSV and check records matched
the notebook. The exporter check confirms that the script and notebook
code agree apart from the intended output-directory assignment.
Each application's `results/` includes `companion.json` and
`migration.json` identifying the checked sources and comparisons.

## Reusable helpers

| Topic | Fresh checks | Evidence |
| --- | --- | --- |
| Transported arithmetic | 14 unit tests and bounded formula checks | [Record](topics/transported_arithmetic/results/verification.json) |
| Parallel resistance | 8 unit tests and workloads of 256 replacements each for 8, 128 and 2048 resistances | [Record](topics/parallel_resistance/results/verification.json) |

These checks ran with CPython 3.14.3 from a temporary working directory.
The published helpers and tests preserve the previous project code's
abstract syntax; the resistance helper has a formatting-only change.
Formula and workload scripts now write beside their topics. Previous
bounded numerical results were reproduced.

The largest observed relative error in the resistance workloads was
`1.7448772222946309e-15` against a fresh conductance sum. This is an
observed result for those inputs, not a general error bound. The tests
include invalid inputs, cancellation rejection and failure atomicity.
A conventional conductance cache has the same asymptotic costs.

## Application observations

| Case | Observed result | Scope |
|---|---|---|
| Gain replacement | 30 → 40 by three routes | Fixed example; tolerance for the logarithmic route. |
| Incremental workload | 256 changes to 16 factors; maximum relative error of the logarithmic route `2.886579864025407e-15` | Powers of two; neither a universal bound nor a timing benchmark. |
| Numerical range | The logarithmic total is retained in the extreme examples | Conversion with `exp` remains limited by the range of `float`. |
| Cancellation in the maintained state | Incremental: `1.0`; rebuilt: `1.00000000000001` | Repair checked for this example; rebuilding costs O(n). |
| Noiseless power law | A ≈ 3, b = 1.5 | Educational identity and conventional log-log regression. |
| Fixed errors on the logarithmic scale | A ≈ 3.153813, b ≈ 1.49 | The errors were chosen; they are not evidence of normality. |
| Two least-squares criteria | Original scale: 4; logarithmic scale: ≈ 2.620741 | Distinct objectives even with the exponent fixed. |

The CSV tables retain the figures displayed, rounded for readability.
Each notebook's code and `checks.json` give access to values at higher
precision. These examples do not validate an empirical mechanism, a
production implementation or a live Colab session.

The original Spanish revision was checked with CPython 3.12.14 and
3.14.3. Those records remain historical evidence in Git history and are
not evidence of checks on this English revision. Consult
[snapshots and records](REPRODUCIBILITY.md#snapshots-and-execution-records) before
interpreting records from an earlier revision.
