# Concept index for Alphy and other agents

Working source: [JulTob/--Calculus](https://github.com/JulTob/--Calculus),
`main` branch. Read by concept and check the scope of the evidence before
reusing a claim. This index guides consultation of the content; it does
not establish that an agent is installed or has executed.

## Concepts and reading routes

- **Exponential generator and positive composition.** Start with the
  definitions and provenance in [sources](sources.md#alpha-framework).
  Then read sections 1 and 2 of
  [gain chains](../notebooks/gain_chains.ipynb): `alpha = exp` makes
  transported addition of positive values equivalent to multiplication.
- **Incremental state, numerical range and precision.** Follow steps
  3–5 and the cancellation limitation in the same notebook. Consult its
  [checks](../results/gain_chains/checks.json) and the
  [results summary](results.md). Maintaining state provides the update
  cost; product/quotient and the same conventional logarithmic method
  are appropriate baselines.
- **Function transport and elasticity.** Read step 1 of
  [power laws and elasticity](../notebooks/power_laws_and_elasticity.ipynb)
  alongside the [composition annotations](local_annotations.md).
  For a positive power law, the log-log slope is `b`, while the Alpha
  derivative is `exp(b)`. These are distinct quantities.
- **Fitting and returning to the original scale.** Continue with steps
  2–4 and the limitations in the power-law notebook. Consult its
  [checks](../results/power_laws_and_elasticity/checks.json).
  Changing scale changes the error criterion. The stated relation
  between mean and median holds only under the declared lognormal model.

The two notebooks are standalone: each application has its own Colab
link, references and results directory. The
[sources.json](../sources.json) catalogue identifies source paths and
roles; it does not replace reading their conditions.

## Primary references and original work

[Sources and provenance](sources.md) records the consulted passages of
Georgiev and Aydin, *Alpha Calculus* (2026), alongside Python,
NIST/SEMATECH and Colab documentation. These are external primary
references for the definitions, models and tools identified there. The
repository neither distributes the book nor claims to have reviewed it
in full.

The notebooks, examples, educational derivations, code and results are
this project's own work. The [local annotations](local_annotations.md)
are reader observations awaiting editorial confirmation, rather than
official errata. Do not attribute the applications to the book or infer
scientific priority from their inclusion here.

## Assumptions, evidence and status

**Demonstrated in these examples:** identities and assertions for two
positive cases, local Python reproduction and separate tables. The
records are described in [results](results.md) and
[environment](environment.md). Saved outputs are evidence for the
snapshots identified by their hashes; they are not a current execution
by an agent consulting them.

**Proposed:** an application to a relevant public workload for gain
chains, and empirical validation of power laws with public data. There
is no timing benchmark, validation of an empirical mechanism or
production implementation yet.

Respect these limitations when extrapolating:

- Logarithms require positive quantities. Modelling uses dimensionless
  ratios and fixed reference quantities.
- An algebraic identity does not impose a noise model or by itself
  improve the estimator, inference or prediction.
- The gain workload uses powers of two. It does not prove error bounds
  for arbitrary `float` factors. Rebuilding the state costs O(n).
- Numerical assertions check the examples. They do not establish
  general stability, novelty or an exclusive advantage over the
  conventional method.
- Local execution uses the standard-library runner. It does not
  establish a live Colab session, a Jupyter kernel or an installed agent.

## Proposing reusable material

Prepare a short, reviewable file or change proposal. Include:

1. The concept and concrete problem, with a situation that makes it
   recognisable.
2. The observable, units, domain, generator and inverse, where relevant.
3. A primary source with an exact location. Distinguish quotations,
   original derivations, local annotations and hypotheses.
4. Intermediate steps and the result on the original scale, with
   assumptions.
5. A competent baseline, expected benefit, full cost and a limitation or
   counterexample that could refute the advantage.
6. Executable evidence, a notebook or test path, and its status:
   `proposed`, `demonstrated in an example` or `validated with data`.
7. The suggested destination and what it adds to existing content.

For another application, propose a standalone notebook with its own
Colab link. For reusable knowledge, first propose a short text in
`docs/` linked to the evidence. Julio decides acceptance and publication
in the Wiki. Preparing a proposal or pull request does not authorise a
Wiki edit or make the content approved canon.
