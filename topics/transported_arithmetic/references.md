# References for transported arithmetic

These routes retain the selected source coverage from the project's
29 October 2026 review. Preparing this topic did not reread the whole book
or conduct a new literature review. The explanations, code and cross-topic
examples are original project material; they are not examples attributed
to the book unless explicitly identified below.

| Consult this concept | Source and locator | Use in this topic |
| --- | --- | --- |
| Generators, transported operations and identities | Svetlin G. Georgiev and Muhittin Evren Aydin, *Alpha Calculus*, first edition, 2026, [DOI 10.1201/9781003750734](https://doi.org/10.1201/9781003750734); printed pp. 1–4, supplied PDF pp. 10–13 | The algebraic framework implemented by the scalar helper. |
| Function transport in both directions | *Alpha Calculus*, printed p. 128 and pp. 131–133; PDF p. 137 and pp. 140–142 | Distinguish `u=alpha o F o alpha^-1` from `F=alpha^-1 o u o alpha`. |
| Derivative and composition order | *Alpha Calculus*, printed pp. 168–170; PDF pp. 177–179, equations 5.1–5.2 and Example 5.1.2 | Basis for the bounded composition check and [local annotations](local_annotations.md). |
| Integration and inverse-hyperbolic-tangent factor | *Alpha Calculus*, printed pp. 265–266; PDF pp. 274–275, Definitions 7.1.1–7.1.2 and Example 7.1.4 | Local derivative-factor annotation and constant-integrand counterexample. |
| Numerical logarithms, exponentials and inverse hyperbolic functions | [Python 3.14 `math`](https://docs.python.org/3.14/library/math.html): `log`, `log1p`, `exp`, `expm1`, `atanh`, `fsum`, `isclose` | Implementation conventions, finite range and floating-point limits. The execution record identifies the actual local runtime. |
| Link, inverse link and response derivative | [R `stats::family`](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html) and [R `stats::make.link`](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/make.link.html): `linkfun`, `linkinv`, `mu.eta` | Distinguish a link-coordinate reading from the ordinary derivative of a response mean. This topic does not run R or fit the user's GLM. |
| Information units and binary entropy | Claude E. Shannon, *A Mathematical Theory of Communication* (1948), [corrected reprint hosted by Purdue](https://engineering.purdue.edu/~mrb/resources/InfoF/Shannon_A-Mathematical-Theory-of-Communication.pdf), reprint p. 1 and section 6, p. 11, Theorem 2 | Definitions supporting the project's derivation of log-odds as a difference of surprisals. That identity is not attributed as a quotation or theorem from Alpha Calculus. |
| Positive reciprocal composition | Karl K. Berggren, [MIT 6.200: Beginning Circuit Analysis](https://circuits.mit.edu/_static/S23/handouts/lec02a/lecture02a.pdf), 14 February 2023, p. 7, ‘Conductance’ | Physical relation behind the separately [implemented resistance topic](../parallel_resistance/README.md). |

PDF page numbers count from 1 in the supplied edition. The original books,
private file paths and page images are not distributed. Source annotations
remain local observations awaiting editorial confirmation, not official
errata. The linked R documentation is R-devel and does not specify a local
executed R version.

Related application routes: [gain chains](../gain_chains/README.md) for
maintained logarithmic coordinates; [power laws](../power_laws/README.md)
for dimensionless elasticity, model assumptions and a complete notebook.
