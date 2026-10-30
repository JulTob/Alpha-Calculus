# Ɑ Calculus

Alpha Calculus experiments and applications.

Representation for understanding and computation.

An educational laboratory for recognising problems in which an Alpha
representation makes a useful structure explicit. Each case starts with
a concrete situation, shows the intermediate steps and compares the
result with an appropriate conventional solution.

The first case studies **chains of positive gains**. Products become
sums of logarithms: contributions can be explained, one stage can be
updated, and the logarithm of a total can be retained beyond the range
of `float`. A loss of precision is also reproduced to show when the
maintained state needs to be rebuilt.

The reduction in update cost comes from maintaining state: a
product/quotient method has the same order of cost per update. This is
not a new algorithm or an advantage exclusive to Alpha Calculus.

The second case studies **power laws and elasticity**. A positive curve
becomes a straight line on logarithmic axes. Its slope is interpreted,
and the example shows why transforming the response changes the error
criterion. The mean and median of the lognormal model are distinguished.

## Start here

Choose an application: **each notebook is a standalone Colab notebook**.

- [Gain chains](notebooks/gain_chains.ipynb): multiplicative composition,
  local changes, numerical range and precision.
  [Open in Colab](https://colab.research.google.com/github/JulTob/Alpha-Calculus/blob/main/notebooks/gain_chains.ipynb).
- [Power laws and elasticity](notebooks/power_laws_and_elasticity.ipynb):
  log-log linearisation, elasticity and fitting assumptions.
  [Open in Colab](https://colab.research.google.com/github/JulTob/Alpha-Calculus/blob/main/notebooks/power_laws_and_elasticity.ipynb).

Either notebook can be uploaded on its own. It requires only Python
3.10 or later and the standard library. It does not depend on the other
notebook, download books, use private data or request access to Drive.

Each Colab link opens the selected application from the `main` branch of
[JulTob/Alpha-Calculus](https://github.com/JulTob/Alpha-Calculus). Select
**Runtime → Run all**. Alternatively, download an `.ipynb` file and select
**File → Upload notebook**.
[Colab documents notebook uploads and the Jupyter
format](https://research.google.com/colaboratory/faq.html).

## Learning objectives

1. Recognise the composition operation and choose consistent coordinates.
2. Distinguish mathematical equality, numerical representation and model
   assumptions.
3. Compare an Alpha proposal with a competent baseline.
4. Check the example, its domains and its limitations.

The reading sequence is **situation → recognition → assumptions → steps →
example → checks and limitations**. Familiarity with logarithms,
functions and basic Python is assumed.

## Reproduce locally

From this directory:

```sh
python3 -B scripts/run_notebooks.py
```

With no arguments, the runner executes both notebooks, each in a new
process. To run a single application:

```sh
python3 -B scripts/run_notebooks.py gains
python3 -B scripts/run_notebooks.py power-laws
```

The runner executes the Python cells in order and saves their outputs
in each notebook. It is a local runner: it does not start a Jupyter
kernel or test a Colab server. The notebooks avoid IPython magics and
syntax specific to IPython.

Numerical results, CSV tables and records are stored separately in
`results/gain_chains/` and `results/power_laws_and_elasticity/`.
Each execution record identifies the runtime and the hash of the
executed notebook. See the [results](docs/results.md),
[environment](docs/environment.md) and
[sources and their scope](docs/sources.md).

## Reading and reuse by agents

The [concept index](docs/index.md) directs Alphy and other agents to
definitions, examples, evidence and limitations. The
[sources.json](sources.json) catalogue locates these sources and
distinguishes primary references from original notes and demonstrations.

## Editorial status

This is the [JulTob/Alpha-Calculus](https://github.com/JulTob/Alpha-Calculus)
repository. Both cases are reproducible educational demonstrations;
there are no empirical data validating a specific application yet.
Extensions and potential Wiki entries are prepared for Julio's review
under the [proposal process](docs/index.md#proposing-reusable-material).

No live Colab session has been tested. No licence has been selected, and
the full text of the book is not distributed. The manifest describes a
file snapshot; see [how to maintain it](docs/environment.md#snapshots-and-execution-records).
The repository follows the [editorial style](docs/editorial_style.md).
