# Fuentes y procedencia

Fecha de comprobación: 29 de octubre de 2026. Las siguientes fuentes
se consultaron en los apartados indicados. No se afirma haber leído
todo el libro ni revisado exhaustivamente la literatura.

## Marco Alpha

Svetlin G. Georgiev y Muhittin Evren Aydin, *Alpha Calculus*, primera
edición, 2026. [Ficha editorial y DOI
10.1201/9781003750734](https://www.routledge.com/Alpha-Calculus/Georgiev-Aydin/p/book/9781003750734).

Se cotejó el texto de las páginas impresas **1–2**, **128** y **169–170**,
páginas **10–11**, **137** y **178–179** del PDF suministrado:
Definiciones 1.1.1, 1.1.5 y 4.1.1, Ejemplo 1.1.3 y ecuaciones 5.1–5.2
con el Ejemplo 5.1.2. Se usan el generador exponencial, su inversa, la suma
transportada y la dirección del transporte de funciones. No se
redistribuye el PDF. Las [correcciones locales](correcciones.md)
se distinguen del texto editorial y de las derivaciones de los tutoriales.

Cada cuaderno incluye sus propias referencias para poder consultarlo por
separado: ganancias usa las operaciones de pp. 1–2; potencias utiliza
además el transporte de funciones, derivada y fuentes de modelado.

Con estas definiciones, la identidad

$$x\oplus_\alpha y=\exp(\log x+\log y)=xy$$

es una derivación directa para positivos. La cadena de ganancias, su
workload y la explicación didáctica son elaboración propia de este
proyecto, apoyada en una demostración local anterior; no son un caso
que atribuyamos al libro ni una novedad científica reivindicada.

## Implementación y reproducción

- [Python 3.14: `math`](https://docs.python.org/3.14/library/math.html),
  apartados `log`, `exp`, `fsum`, `prod`, `isclose` e implementación
  subyacente. Se consultaron las definiciones, las advertencias de
  precisión de `fsum` y las excepciones del módulo. La documentación
  servida identifica una revisión de Python 3.14 distinta del parche
  local; el runtime ejecutado queda en `resultados/<aplicación>/ejecucion.json`.
- [Google Colab: preguntas frecuentes](https://research.google.com/colaboratory/faq.html),
  apartados «Using Colab», importación de cuadernos, salidas compartidas
  y runtime. Se usa para las instrucciones de carga, no como evidencia
  de haber ejecutado los cuadernos en Colab.

## Modelado de leyes de potencia

- [NIST/SEMATECH, 2.3.6.1: Models for instrument
  calibration](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc361.htm),
  apartado «Power model treated as a linear model», consultado completo.
  Fundamenta la relación entre errores multiplicativos y linealización
  logarítmica. La lectura Alpha, las referencias adimensionales y los
  datos de demostración son nuestra exposición.
- [NIST/SEMATECH, 1.3.6.6.9: Lognormal
  Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3669.htm),
  parametrización y «Common Statistics», consultados completos. Se usan
  para distinguir mediana y media al volver de la escala logarítmica.
- [NIST/SEMATECH, 4.4.5.3: Accounting for Errors with a Non-Normal
  Distribution](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd453.htm),
  «Using Transformations». Apoya separar elección de transformación,
  ajuste y validación del modelo; no certifica los datos de este tutorial.

El resultado exacto del baseline producto/cociente se comprueba en un
workload de **potencias de dos**. No se extrapola a factores float
arbitrarios. Los contraejemplos de rango y cancelación se ejecutan de
nuevo dentro del tutorial. Las aserciones numéricas no sustituyen las
derivaciones algebraicas ni prueban cotas generales de error.

## Publicación y posibles ampliaciones

Las hipótesis futuras deben etiquetarse como propuestas y comprobarse
contra un baseline. Una elección de coordenadas no basta para establecer
un nuevo modelo estadístico, una teoría física o una mejora algorítmica.
La elección de licencia corresponde al autor del repositorio.
