# Resultados reproducidos

Cada aplicación se ejecutó por separado en CPython **3.12.14** y
**3.14.3**, con un espacio de nombres nuevo en cada proceso:

| Cuaderno autónomo | Celdas totales | Celdas Python | Registro |
|---|---:|---:|---|
| Cadenas de ganancias | 20 | 10 | [Ejecución](../resultados/cadenas_de_ganancias/ejecucion.json) |
| Potencias y elasticidad | 23 | 13 | [Ejecución](../resultados/potencias_y_elasticidad/ejecucion.json) |

Pasaron todas las comprobaciones. Cada cuaderno conserva las salidas de
su ejecución 3.14.3 y sus tablas, resultados y registros en una subcarpeta
propia. Se probó además cada `.ipynb` solo, copiado a un directorio vacío,
sin el otro cuaderno ni archivos del workspace.

| Caso | Resultado observado | Alcance |
|---|---|---|
| Sustitución de ganancias | 30 → 40 por tres rutas | Ejemplo fijo; tolerancia para la ruta logarítmica. |
| Workload incremental | 256 cambios sobre 16 factores; error relativo máximo log de `2.886579864025407e-15` | Potencias de dos; no cota universal ni benchmark de tiempos. |
| Rango | El log-total se conserva en los ejemplos extremos | Volver con `exp` sigue limitado por el rango de `float`. |
| Cancelación histórica | Incremental: `1.0`; reconstruido: `1.00000000000001` | Reparación comprobada en ese ejemplo; reconstruir cuesta O(n). |
| Potencia sin ruido | A ≈ 3, b = 1.5 | Identidad didáctica y regresión log-log convencional. |
| Errores fijos en log | A ≈ 3.153813, b ≈ 1.49 | Los errores se eligieron; no son evidencia de normalidad. |
| Dos criterios LS | Original: 4; log: ≈ 2.620741 | Distintos objetivos incluso con exponente fijado. |

Las tablas CSV conservan las cifras mostradas, redondeadas para lectura.
El código de cada cuaderno y su `comprobaciones.json` permiten consultar los
valores de mayor precisión. No se afirma haber validado un mecanismo
empírico, una implementación de producción o una sesión Colab en vivo.


Los registros anteriores se conservan como evidencia histórica de la
preparación original. `ejecucion.json` corresponde al cuaderno guardado;
las ejecuciones de otras versiones pueden tener hashes diferentes por
sus salidas. Los registros de estructura, independencia y ZIP no se
regeneran al ejecutar el tutorial: consulta
[instantáneas y registros](entorno.md#instantáneas-y-registros) antes de
interpretarlos como evidencia de una revisión posterior.
