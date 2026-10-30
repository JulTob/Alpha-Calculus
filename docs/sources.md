# Sources and provenance

Source check date: 29 October 2026. The sources below were consulted in
the sections identified. This does not imply that the whole book was
read or that the literature was reviewed exhaustively.

## Alpha framework

Svetlin G. Georgiev and Muhittin Evren Aydin, *Alpha Calculus*, first
edition, 2026. [Publisher's record and DOI
10.1201/9781003750734](https://www.routledge.com/Alpha-Calculus/Georgiev-Aydin/p/book/9781003750734).

The text on printed pages **1–2**, **128** and **169–170** was checked
against pages **10–11**, **137** and **178–179** of the supplied PDF:
Definitions 1.1.1, 1.1.5 and 4.1.1, Example 1.1.3, and equations 5.1–5.2
with Example 5.1.2. The tutorials use the exponential generator, its
inverse, transported addition and the direction of function transport.
The PDF is not redistributed. The [local annotations](local_annotations.md)
are distinguished from the published text and the tutorials' derivations.

Each notebook includes its own references so that it can be read
independently: gain chains uses the operations on pages 1–2; power laws
also uses function transport, differentiation and modelling sources.

Under these definitions, the identity

$$x\oplus_\alpha y=\exp(\log x+\log y)=xy$$

is a direct derivation for positive values. The gain chain, its workload
and the educational explanation are original work by this project,
supported by an earlier local demonstration. They are not an application
attributed to the book or a claim of scientific novelty.

## Implementation and reproduction

- [Python 3.14: `math`](https://docs.python.org/3.14/library/math.html),
  sections on `log`, `exp`, `fsum`, `prod`, `isclose` and the underlying
  implementation. The definitions, `fsum` precision warnings and module
  exceptions were consulted. The documentation served identifies a
  Python 3.14 revision different from the local patch release; the
  executed runtime is recorded in
  `results/<application>/execution.json`.
- [Google Colab: frequently asked
  questions](https://research.google.com/colaboratory/faq.html), sections
  on ‘Using Colab’, notebook imports, shared outputs and runtimes. These
  support the upload instructions; they are not evidence of a notebook
  execution in Colab.

## Power-law modelling

- [NIST/SEMATECH, 2.3.6.1: Models for instrument
  calibration](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc361.htm),
  ‘Power model treated as a linear model’, consulted in full. This
  supports the relation between multiplicative errors and logarithmic
  linearisation. The Alpha interpretation, dimensionless reference
  quantities and demonstration data are this project's presentation.
- [NIST/SEMATECH, 1.3.6.6.9: Lognormal
  Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3669.htm),
  the parametrisation and ‘Common Statistics’, consulted in full. These
  are used to distinguish the median and mean when returning from the
  logarithmic scale.
- [NIST/SEMATECH, 4.4.5.3: Accounting for Errors with a Non-Normal
  Distribution](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd453.htm),
  ‘Using Transformations’. This supports distinguishing the choice of
  transformation, fitting and model validation; it does not validate
  the tutorial's data.

The exact result for the product/quotient baseline is checked on a
workload of **powers of two**. It is not extrapolated to arbitrary
floating-point factors. The numerical range and cancellation
counterexamples are executed within the tutorial. Numerical assertions
do not replace algebraic derivations or prove general error bounds.

## Publication and possible extensions

Future hypotheses must be labelled as proposals and checked against a
competent baseline. A coordinate choice alone does not establish a new
statistical model, a physical theory or an algorithmic improvement.
The repository author decides which licence to select.
