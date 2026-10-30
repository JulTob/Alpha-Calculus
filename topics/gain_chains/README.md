# Gain chains

Use this topic when positive, finite, dimensionless factors multiply and
a known stage changes repeatedly. The logarithmic coordinates expose
each contribution and the effect of a local replacement.

1. Read [the standalone notebook](notebook.ipynb) for the derivation,
   worked steps and exercises. [Open it in Colab](https://colab.research.google.com/github/JulTob/Alpha-Calculus/blob/main/topics/gain_chains/notebook.ipynb).
2. Run [the Python companion](example.py) to reproduce the same code
   without a notebook interface:

   ```sh
   python3 -B topics/gain_chains/example.py
   ```

3. Inspect [the numerical checks](results/checks.json),
   [execution record](results/execution.json) and
   [references](references.md).

The script writes to this topic's `results/` directory, regardless of
the current working directory. A downloaded notebook writes to
`results/` in its runtime's working directory. It needs only Python's
standard library and can be uploaded without the repository.

The notebook is the maintained calculation source. The companion is
generated with `python3 -B maintenance/export_examples.py`; check it with
the same command followed by `--check`. Both contain the same numerical
code, with only the output-directory assignment adapted for the script.

## What the checks establish

The fixed replacement gives 30 → 40 by recomputation, product/quotient
and logarithmic state. A reproducible workload checks 256 changes to 16
powers-of-two factors. Further examples expose overflow, underflow and
cancellation in a maintained accumulator.

Maintained product/quotient and logarithmic state both give O(1) work
per replacement and query after O(n) preparation. Conventional maintained
logarithms are the same algorithm. These demonstrations establish no
exclusive Alpha speed-up or general floating-point error bound.

The original earlier short demo repeats this notebook's 30 → 40
calculation and is not maintained as a separate public implementation.
For source and runtime boundaries, see [reproducibility](../../REPRODUCIBILITY.md).
