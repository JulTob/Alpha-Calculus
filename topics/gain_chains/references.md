# Gain-chain references

## Primary framework

Svetlin G. Georgiev and Muhittin Evren Aydin, *Alpha Calculus*,
first edition, 2026. [DOI 10.1201/9781003750734](https://doi.org/10.1201/9781003750734).

Consulted during the earlier preparation: printed **pp. 1–2** /
supplied PDF **pp. 10–11**, Definitions 1.1.1 and 1.1.5 and Example
1.1.3. These locate the generator, transported addition and exponential
example. For positive values, this topic derives

$$x\oplus_\alpha y=\exp(\log x+\log y)=xy.$$

The gain-chain application, replacement workload, exercises and code
are this project's original educational exposition. They are not
attributed to the book as an application or a novel algorithm.
The book is not redistributed.

## Implementation

[Python 3.14, `math`](https://docs.python.org/3.14/library/math.html):
`log`, `exp`, `fsum`, `prod` and `isclose`, including module exceptions
and the `fsum` precision caveats. These passages were consulted during
preparation; the runtime actually executed is recorded separately in
[results/execution.json](results/execution.json).

The notebook and script execute their own fixed numerical checks.
The powers-of-two workload does not establish accuracy for arbitrary
factors. Rebuilding repairs the displayed cancellation example and costs
O(n); no universal error bound is claimed.

## Reproduction

[Google Colab FAQ](https://research.google.com/colaboratory/faq.html):
notebook loading, shared outputs and runtimes, consulted during earlier
preparation. This supports the upload route, not a live Colab test.
The current migration is a local reorganisation and rerun of the
existing tutorial, not a new literature review.
