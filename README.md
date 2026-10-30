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

Choose a topic. Its explanation, references, scripts, tests and results
are kept together.

| Topic | Runnable code | Reading route |
| --- | --- | --- |
| Transported arithmetic | [Scalar helper](topics/transported_arithmetic/alpha_transport.py) and formula checks | [Guide and references](topics/transported_arithmetic/README.md) |
| Gain chains | [Standalone example](topics/gain_chains/example.py) | [Guide and references](topics/gain_chains/README.md) |
| Power laws and elasticity | [Standalone example](topics/power_laws/example.py) | [Guide and references](topics/power_laws/README.md) |
| Parallel resistance | [Incremental helper](topics/parallel_resistance/parallel_resistance.py) and workload | [Guide and references](topics/parallel_resistance/README.md) |

The arithmetic helper covers identity, exponential and inverse-logit
generators. The resistance helper maintains a fixed bank of positive
finite resistances. Each has focused tests and explicit domain checks.
These are bounded educational implementations. A conventional
conductance cache matches the resistance helper's asymptotic cost.

**Each application notebook is a standalone Colab notebook**.

- [Gain chains](topics/gain_chains/notebook.ipynb): multiplicative composition,
  local changes, numerical range and precision.
  [Open in Colab](https://colab.research.google.com/github/JulTob/Alpha-Calculus/blob/main/topics/gain_chains/notebook.ipynb).
- [Power laws and elasticity](topics/power_laws/notebook.ipynb):
  log-log linearisation, elasticity and fitting assumptions.
  [Open in Colab](https://colab.research.google.com/github/JulTob/Alpha-Calculus/blob/main/topics/power_laws/notebook.ipynb).

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
python3 -B maintenance/run_notebooks.py
```

With no arguments, the runner executes both notebooks, each in a new
process. To run a single application:

```sh
python3 -B maintenance/run_notebooks.py gains
python3 -B maintenance/run_notebooks.py power-laws
```

The runner executes the Python cells in order and saves their outputs
in each notebook. It is a local runner: it does not start a Jupyter
kernel or test a Colab server. The notebooks avoid IPython magics and
syntax specific to IPython.

Numerical results, CSV tables and records are stored with their topic in
`topics/<topic>/results/`.
Each execution record identifies the runtime and the hash of the
executed notebook. See the [results](RESULTS.md),
[environment](REPRODUCIBILITY.md) and
[sources and their scope](SOURCES.md).

To use the code without a notebook interface:

```sh
python3 -B topics/gain_chains/example.py
python3 -B topics/power_laws/example.py
python3 -B topics/transported_arithmetic/check_formulas.py
python3 -B topics/parallel_resistance/run_workload.py
```

The application scripts are generated from their notebooks. Edit the
notebook, then use `maintenance/export_examples.py` to keep the two
forms consistent. Shared repository maintenance belongs in
`maintenance/`; mathematical code belongs with its topic.

## Reading and reuse by agents

The [concept index](CONCEPTS.md) directs Alphy and other agents to
definitions, examples, evidence and limitations. The
[sources.json](sources.json) catalogue locates these sources and
distinguishes primary references from original notes and demonstrations.

## Editorial status

This is the [JulTob/Alpha-Calculus](https://github.com/JulTob/Alpha-Calculus)
repository. Both cases are reproducible educational demonstrations;
there are no empirical data validating a specific application yet.
Extensions and potential Wiki entries are prepared for Julio's review
under the [proposal process](CONCEPTS.md#proposing-reusable-material).

No live Colab session has been tested. No licence has been selected, and
the full text of the book is not distributed. The manifest describes a
file snapshot; see [how to maintain it](REPRODUCIBILITY.md#snapshots-and-execution-records).
The repository follows the [editorial style](EDITORIAL_STYLE.md).
