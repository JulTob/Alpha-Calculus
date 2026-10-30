# Local annotations on the book

A limited review of *Alpha Calculus*, first edition, 2026, documented
the passages below. These are possible errors checked locally and
awaiting editorial confirmation. They are not official errata or an
assessment of the book as a whole.

| Printed page | PDF page, counting from 1 | Location | Annotation |
|---:|---:|---|---|
| 169 | 178 | First equality under ‘Moreover, we have’ | The subscript is missing from the subtrahend `f_alpha(x)`. The following line includes it. |
| 170 | 179 | Last equality in ‘Consider now…’ | The outer transformation and the transformed argument are lost. |
| 170 | 179 | First line of ‘Using this and (5.2)…’ | The composition inside the derivative is reversed. The following expansion uses the correct order. |
| 266 | 275 | Example 7.1.4 | The derivative factor for `artanh(x)` should be `1/(1-x*x)` on its real domain. |

## Formula used in the tutorial

For a positive function `f: (0, infinity) -> (0, infinity)` and
`alpha = exp`, define directly:

$$F(t)=\log(f(e^t)),\qquad
D_\alpha f(X)=\exp(F'(\log X)).$$

The second equality requires the ordinary derivative of `F` to exist at
the point. For `f(X)=A*X^b`, with `A>0`, the derivation is explicit:
`F(t)=log(A)+b*t`, so `D_alpha f=exp(b)`.

The representation of the original function is

$$f(X)=\exp(F(\log X)),$$

rather than `f(X)=F(X)`. The composition order inside the derivative is
`alpha^-1 o f o alpha`. These identities were checked against pages 128
and 169–170 and Example 5.1.2 of the original.

The tutorial does not require the integration formulae in Example 7.1.4.
No pages from the book are distributed, and no claim is made that the
authors have confirmed these observations.
