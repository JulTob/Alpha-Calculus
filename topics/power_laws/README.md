# Power laws and elasticity

Use this topic when a positive scaling relation may follow
$Y=AX^b$, with $X$ and $Y$ defined as dimensionless ratios. The
logarithmic slope explains elasticity; the noise model and fitting
criterion still require separate decisions.

1. Read [the standalone notebook](notebook.ipynb) for derivation,
   fitting, interpretation and exercises. [Open it in Colab](https://colab.research.google.com/github/JulTob/Alpha-Calculus/blob/main/topics/power_laws/notebook.ipynb).
2. Run [the Python companion](example.py) to reproduce the same code:

   ```sh
   python3 -B topics/power_laws/example.py
   ```

3. Inspect [the numerical checks](results/checks.json),
   [execution record](results/execution.json) and
   [references](references.md).

The script writes to this topic's `results/` directory from any working
directory. The notebook requires only the standard library and can be
uploaded by itself; its `results/` directory is created in the runtime's
working directory.

The notebook is the maintained calculation source. Regenerate the
companion with `python3 -B maintenance/export_examples.py`, or append
`--check` to check synchronisation. Only the output-directory assignment
differs between their numerical code.

## What the checks establish

For $\alpha=\exp$, the transported function is
$F(t)=\log A+bt$. The elasticity is $b$, while the Alpha derivative is
$e^b$. The code recovers a noiseless fixed example and fits another
example with chosen errors. It distinguishes log-scale least squares
from original-scale least squares, the lognormal mean from the median,
and positive observations from data outside the logarithm's domain.

This is conventional log-log fitting expressed through Alpha coordinates.
The examples do not validate an empirical law or establish a new
estimator. The [local source annotations](../transported_arithmetic/local_annotations.md)
are reader findings pending editorial confirmation.
See [reproducibility](../../REPRODUCIBILITY.md) for execution scope.
