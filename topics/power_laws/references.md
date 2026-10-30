# Power-law references

## Primary framework

Svetlin G. Georgiev and Muhittin Evren Aydin, *Alpha Calculus*,
first edition, 2026. [DOI 10.1201/9781003750734](https://doi.org/10.1201/9781003750734).

Consulted during the earlier preparation: printed **pp. 1–2**
(generator), **p. 128** (Definition 4.1.1), **pp. 169–170**
(equations 5.1–5.2 and Example 5.1.2). Their supplied-PDF locations
are pp. **10–11**, **137** and **178–179**.

This topic derives $F=\alpha^{-1}\circ f\circ\alpha$ directly.
Local omissions and a reversed composition on pp. 169–170 remain
[reader annotations](../transported_arithmetic/local_annotations.md)
pending editorial confirmation. The reversed equality is not used.
The book is not redistributed.

## Statistical modelling

- [NIST/SEMATECH 2.3.6.1, Models for instrument calibration](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc361.htm):
  “Power model treated as a linear model”, consulted during preparation.
  Supports logarithmic linearisation under multiplicative error.
- [NIST/SEMATECH 1.3.6.6.9, Lognormal Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3669.htm):
  parametrisation and “Common Statistics”, consulted during preparation.
  Supports the distinction between median and mean. The conditional
  application here explicitly states its assumptions.
- [NIST/SEMATECH 4.4.5.3, Accounting for Errors with a Non-Normal Distribution](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd453.htm):
  “Using Transformations”, consulted during preparation. Supports
  distinguishing transformation from model validation.

Dimensionless reference quantities, fixed data, derivations and code
are this project's original educational exposition. No empirical model
validation, exclusive Alpha improvement or scientific priority is claimed.

## Implementation and reproduction

[Python 3.14, `math`](https://docs.python.org/3.14/library/math.html):
`log`, `exp`, `fsum` and `isclose`, consulted during preparation.
The actual local runtime is recorded in
[results/execution.json](results/execution.json).

[Google Colab FAQ](https://research.google.com/colaboratory/faq.html):
notebook loading, shared outputs and runtimes, consulted during earlier
preparation. This supports the upload route, not a live Colab test.
The migration reruns the existing tutorial locally and does not claim
new external source consultation.
