# References for parallel resistance

| Consult this concept | Source and locator | Role and boundary |
| --- | --- | --- |
| Conductance as reciprocal resistance and addition in parallel | Karl K. Berggren, [MIT 6.200: Beginning Circuit Analysis](https://circuits.mit.edu/_static/S23/handouts/lec02a/lecture02a.pdf), 14 February 2023, p. 7, ‘Conductance’ | Physical relation reviewed by the project on 29 October 2026. The restricted transport and incremental implementation are the project's derivation. |
| Transported operations through a generator | Svetlin G. Georgiev and Muhittin Evren Aydin, *Alpha Calculus*, first edition, 2026, [DOI 10.1201/9781003750734](https://doi.org/10.1201/9781003750734), printed pp. 1–4, supplied PDF pp. 10–13 | General framework. The positive reciprocal is a restricted analogue; it is not asserted to satisfy the book's generator-on-all-reals definition. See [transported arithmetic](../transported_arithmetic/README.md). |
| Careful floating-point summation, finite values and comparison | [Python 3.14 `math`](https://docs.python.org/3.14/library/math.html), `fsum`, `isfinite`, `isclose` and summation warnings | Implementation and numerical comparison. `fsum` cannot reconstruct information already lost from a rounded cached total. |
| Machine epsilon | [Python 3.14 `sys.float_info`](https://docs.python.org/3.14/library/sys.html#sys.float_info) | Definition of the runtime quantity used by the conservative cancellation guard; not a general accuracy certificate. |

The project previously checked the indicated source sections. This
publication adds runnable code, original explanation, tests and a fresh
bounded workload, rather than a new literature review. No book pages or
private source files are redistributed.

The algorithm, workload seeds, traces, conservative rejection policy and
complexity comparison are original project material. No source is being
credited with a promise of computational superiority. A conventional
conductance cache has the same asymptotic performance.
