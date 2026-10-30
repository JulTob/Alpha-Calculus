# Índice por conceptos para Alphy y otros agentes

Fuente de trabajo: [JulTob/--Calculus](https://github.com/JulTob/--Calculus),
rama `main`. Lee por concepto y comprueba el alcance de la evidencia antes
de reutilizar una afirmación. Este índice orienta la consulta del contenido;
por sí solo no acredita instalación ni ejecución de un agente.

## Conceptos y rutas de lectura

- **Generador exponencial y composición positiva.** Empieza por las
  definiciones y la procedencia en [fuentes](fuentes.md#marco-alpha).
  Después lee las secciones 1 y 2 de
  [cadenas de ganancias](../notebooks/cadenas_de_ganancias.ipynb):
  `alpha = exp` convierte la suma transportada de positivos en producto.
- **Estado incremental, rango y precisión.** Sigue los pasos 3–5 y el
  límite de cancelación del mismo cuaderno. Consulta sus
  [comprobaciones](../resultados/cadenas_de_ganancias/comprobaciones.json)
  y los [resultados resumidos](resultados.md). El estado mantenido aporta
  el coste por actualización; producto/cociente y el mismo método
  logarítmico convencional son baselines pertinentes.
- **Transporte de funciones y elasticidad.** Lee el paso 1 de
  [potencias y elasticidad](../notebooks/potencias_y_elasticidad.ipynb)
  junto con las [anotaciones de composición](correcciones.md).
  Para una potencia positiva, la pendiente log-log es `b`; la derivada
  Alpha es `exp(b)`. Son cantidades distintas.
- **Ajuste y regreso a la escala original.** Continúa en los pasos 2–4 y
  límites del cuaderno de potencias. Consulta las
  [comprobaciones](../resultados/potencias_y_elasticidad/comprobaciones.json).
  Cambiar escala modifica el criterio de error; media y mediana sólo
  tienen la relación indicada bajo el modelo lognormal declarado.

Los dos cuadernos son autónomos: cada aplicación tiene su propio Colab,
sus referencias y su carpeta de resultados. El catálogo
[sources.json](../sources.json) identifica las rutas y los papeles de las
fuentes; no sustituye la lectura de sus condiciones.

## Referencias primarias y elaboración original

[Fuentes y procedencia](fuentes.md) registra los pasajes consultados de
Georgiev y Aydin, *Alpha Calculus* (2026), junto con la documentación de
Python, NIST/SEMATECH y Colab. Son referencias externas primarias para
las definiciones, modelos y herramientas allí identificados. El repositorio
no distribuye el libro ni afirma haberlo revisado en su totalidad.

Los cuadernos, sus ejemplos, derivaciones didácticas, código y resultados
son elaboración de este proyecto. Las
[anotaciones locales](correcciones.md) son observaciones del lector,
pendientes de confirmación editorial: no son una fe de erratas oficial.
No atribuyas los casos de aplicación al libro ni les atribuyas prioridad
científica por aparecer aquí.

## Supuestos, evidencia y estado

**Demostrado en estos ejemplos:** identidades y aserciones de dos casos
positivos; reproducción local con Python y tablas independientes. Los
registros conservados están descritos en [resultados](resultados.md) y
[entorno](entorno.md). Las salidas guardadas son evidencia de las
instantáneas identificadas por sus hashes, no una ejecución actual del
agente que las consulta.

**Propuesto:** una aplicación a un workload público pertinente para
las ganancias y una validación empírica de potencias con datos públicos.
Todavía no hay benchmark de tiempos ni validación de un mecanismo
empírico o una implementación de producción.

Respeta estos límites al extrapolar:

- Los logaritmos requieren cantidades positivas; en el modelado se usan
  razones adimensionales y referencias fijas.
- La identidad algebraica no impone un modelo de ruido ni mejora por sí
  sola el estimador, la inferencia o la predicción.
- El workload de ganancias usa potencias de dos; no prueba cotas de error
  para factores `float` arbitrarios. Reconstruir el estado cuesta O(n).
- Las aserciones numéricas comprueban los ejemplos; no prueban estabilidad
  general, novedad ni ventaja exclusiva frente al método convencional.
- La ejecución local usa el ejecutor de biblioteca estándar. No acredita
  una sesión Colab en vivo, un kernel Jupyter ni un agente instalado.

## Proponer contenido reutilizable

Prepara una propuesta breve de archivo o cambio revisable. Incluye:

1. Concepto y problema concreto; situación que permite reconocerlo.
2. Observable, unidades, dominio, generador e inversa, si procede.
3. Fuente primaria con localización exacta; distingue cita, derivación
   propia, corrección local e hipótesis.
4. Pasos intermedios y resultado en la escala original, con supuestos.
5. Baseline competente, beneficio esperado, coste completo y un límite o
   contraejemplo que pueda refutar la ventaja.
6. Evidencia ejecutable, ruta del cuaderno o prueba y estado:
   `propuesto`, `demostrado en ejemplo` o `validado con datos`.
7. Destino sugerido y qué aporta frente al contenido existente.

Si es otra aplicación, propón un cuaderno autónomo y su propio Colab.
Si es conocimiento reutilizable, propón primero un texto pequeño en
`docs/` con vínculos a la evidencia. Julio decide su aceptación y la
publicación en la wiki; preparar una propuesta o un PR no autoriza editar
la wiki ni presentar el contenido como canon aprobado.
