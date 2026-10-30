# Anotaciones locales sobre el libro

La revisión acotada de *Alpha Calculus*, primera edición de 2026,
documentó los pasajes siguientes. Son posibles erratas comprobadas
localmente, pendientes de confirmación editorial; no son una fe de
erratas oficial ni un juicio sobre todo el libro.

| Impresa | PDF, desde 1 | Localización | Anotación |
|---:|---:|---|---|
| 169 | 178 | Primera igualdad bajo «Moreover, we have» | Falta el subíndice en el sustraendo `f_alpha(x)`. La línea siguiente ya lo incluye. |
| 170 | 179 | Última igualdad de «Consider now…» | Se pierden la transformación exterior y el argumento transformado. |
| 170 | 179 | Primera línea de «Using this and (5.2)…» | Dentro de la derivada aparece la composición invertida. La expansión siguiente usa el orden correcto. |
| 266 | 275 | Ejemplo 7.1.4 | El factor de la derivada de `artanh(x)` debe ser `1/(1-x*x)`, en su dominio real. |

## Fórmula usada en el tutorial

Para una función positiva `f: (0, infinito) -> (0, infinito)` y
`alpha = exp`, definimos directamente:

$$F(t)=\log(f(e^t)),\qquad
D_\alpha f(X)=\exp(F'(\log X)).$$

La segunda igualdad requiere que exista la derivada ordinaria de `F`
en el punto. Para `f(X)=A*X^b`, `A>0`, la derivación es explícita:
`F(t)=log(A)+b*t`, por lo que `D_alpha f=exp(b)`.

La representación de la función original es

$$f(X)=\exp(F(\log X)),$$

no `f(X)=F(X)`. El orden de composición dentro de la derivada es
`alpha^-1 o f o alpha`. Estas identidades se contrastaron con las
páginas 128 y 169–170 y con el Ejemplo 5.1.2 del original.

El tutorial no necesita las fórmulas de integración del Ejemplo 7.1.4.
No se distribuyen páginas del libro ni se afirma que los autores hayan
confirmado estas observaciones.
