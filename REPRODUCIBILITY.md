# Environment and reproduction

Each tutorial uses only the Python 3.10+ standard library. It requires no
GPU, credentials, network connection, private files or copy of the book.
Tables are displayed as aligned text and exported to CSV for inspection
or plotting in another tool. NumPy, Matplotlib and a custom plotting
implementation are not required.

## Local checks

```sh
python3 -B maintenance/run_notebooks.py
```

The runner can be invoked from any working directory and executes both notebooks,
each in a separate process. It also accepts `gains` or `power-laws` to
run a single application, or `all` to run both explicitly. Each process
starts with a fresh namespace and executes the code cells in order.
The runner captures `stdout` and `stderr`, retains the execution count
and stops the process if a cell fails. It does not fabricate outputs or
reuse state from another session. Records are stored in
`topics/<topic>/results/`.

These checks validate the Python code and each notebook's assertions.
They do not test the Colab interface or Jupyter extensions. Reading a
notebook with saved outputs is not a new execution.

## Interactive reproduction

Choose an `.ipynb` file, open it in Jupyter or upload it on its own to
Colab, and run all cells in a fresh runtime. The code creates its own
`results/` directory in the current directory. In Colab, these
files belong to the temporary runtime; download any files to be kept.
Neither notebook mounts Drive or needs files from the other notebook.

Both English notebooks passed full and standalone execution with
CPython 3.14.3 on macOS arm64, as described in [results](RESULTS.md).
Earlier CPython 3.12.14 and 3.14.3 checks belong to the original Spanish
revision retained in Git history. The English revision has not been
tested with Python 3.12. No live Colab session or Colab interface has
been tested.

## Dependencies

`requirements.txt` adds no packages to the runtime. A local Jupyter
interface can be installed separately in the user's own environment.
Interface packages are not mathematical dependencies of the examples.

## Topic scripts and helper tests

Each application has an `example.py` companion next to its notebook.
It runs with the standard library and writes to that topic's `results/`
directory, even when invoked from another working directory.
Generate companions after editing notebook code:

```sh
python3 -B maintenance/export_examples.py
python3 -B maintenance/export_examples.py --check
```

Run the bounded helpers' tests and checks from the repository root:

```sh
python3 -B -m unittest discover -s topics/transported_arithmetic
python3 -B topics/transported_arithmetic/check_formulas.py
python3 -B -m unittest discover -s topics/parallel_resistance
python3 -B topics/parallel_resistance/run_workload.py
```

Topic guides describe inputs, intermediate quantities and limitations.
Formula and workload scripts write their records within their own topic.
These checks do not establish general floating-point error bounds or
performance advantages over a conventional maintained-state method.

## Snapshots and execution records

`manifest.json` contains SHA-256 hashes of a reviewed repository snapshot,
excluding the manifest itself. It is not a dynamic execution record.
The runner updates each executed notebook, its tables, `checks.json`
and `execution.json`. Standalone checks are recorded separately in
`standalone.json` when those checks are explicitly run. The runner does
not regenerate `manifest.json` or establish that a standalone check has
been repeated.

The original Spanish revision's runtime, structure, standalone and ZIP
records remain historical evidence in Git history. They identify the
snapshots checked at that time, including a ZIP preparation test.
Notebook outputs include the Python version, so different runtimes can
produce different notebook hashes. An earlier hash is not automatic
evidence for the current file contents.

To check a snapshot without modifying it, run the notebooks in a
temporary copy of the directory. When changing content to be retained:

1. Execute from a fresh process and review the outputs and assertions.
2. Update documentation affected by the results. Keep historical records
   identified as such, or explicitly repeat their checks.
3. Regenerate `manifest.json` for the reviewed files and check that every
   path and hash matches before proposing the change.

The `sources.json` catalogue describes concepts and provenance. It is
not an integrity manifest and does not imply that an external reference
is included in the repository.
