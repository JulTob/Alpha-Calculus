# Ɑ Calculus

Alpha Calculus experiments and applications.

Representar para comprender y calcular.

Un laboratorio didáctico en español para reconocer problemas en los que
una representación Alpha hace explícita una estructura útil. Cada caso
parte de una situación concreta, muestra los pasos intermedios y compara
el resultado con una solución convencional pertinente.

El primer caso estudia **cadenas de ganancias positivas**. Los productos
se convierten en sumas de logaritmos: podemos explicar contribuciones,
actualizar una etapa y conservar el logaritmo de un total fuera del rango
de `float`. También reproducimos una pérdida de precisión para mostrar
cuándo conviene reconstruir el estado.

La ventaja de coste procede de conservar estado: producto/cociente ofrece
el mismo orden de coste por actualización. No presentamos un algoritmo
nuevo ni superioridad exclusiva de Alpha Calculus.

El segundo caso estudia **leyes de potencia y elasticidad**. Pasamos de
una curva positiva a una recta en log-log, interpretamos su pendiente y
comprobamos por qué transformar la respuesta cambia el criterio de error.
Las medias y medianas del modelo lognormal quedan separadas.

## Empieza aquí

Elige una aplicación: **cada cuaderno es un Colab autónomo**.

- [Cadenas de ganancias](notebooks/cadenas_de_ganancias.ipynb):
  composición multiplicativa, cambios locales, rango y precisión.
  [Abrir su Colab](https://colab.research.google.com/github/JulTob/--Calculus/blob/main/notebooks/cadenas_de_ganancias.ipynb).
- [Potencias y elasticidad](notebooks/potencias_y_elasticidad.ipynb):
  linealización log-log, elasticidad y supuestos del ajuste.
  [Abrir su Colab](https://colab.research.google.com/github/JulTob/--Calculus/blob/main/notebooks/potencias_y_elasticidad.ipynb).

Puedes subir cualquiera de los dos por separado. Sólo necesita Python
3.10 o posterior y su biblioteca estándar. No depende del otro cuaderno
ni descarga libros; tampoco usa datos privados ni solicita acceso a Drive.

Cada enlace de Colab abre únicamente la aplicación elegida desde la rama
`main` de [JulTob/--Calculus](https://github.com/JulTob/--Calculus).
Después, selecciona **Entorno de ejecución → Ejecutar todas**. También
puedes descargar un `.ipynb` y usar **Archivo → Subir cuaderno**.
[Colab documenta la carga de cuadernos y su formato
Jupyter](https://research.google.com/colaboratory/faq.html).

## Qué aprenderás

1. Reconocer la operación de composición y elegir coordenadas coherentes.
2. Separar igualdad matemática, representación numérica y supuesto de modelo.
3. Comparar una propuesta Alpha con un baseline competente.
4. Verificar el ejemplo, sus dominios y sus límites.

La ruta de lectura es **situación → reconocimiento → supuestos → pasos →
ejemplo → comprobación y límites**. Se presupone manejo de logaritmos,
funciones y Python básico.

## Reproducir localmente

Desde esta carpeta:

```sh
python3 -B scripts/ejecutar_notebook.py
```

Sin argumentos ejecuta ambos, cada uno en un proceso nuevo. Para ejecutar
sólo una aplicación:

```sh
python3 -B scripts/ejecutar_notebook.py ganancias
python3 -B scripts/ejecutar_notebook.py potencias
```

El programa ejecuta las celdas Python en orden y conserva sus salidas en
cada cuaderno. Es un ejecutor local: no arranca un kernel Jupyter ni prueba
un servidor Colab. Los cuadernos evitan magias y sintaxis exclusiva de IPython.

Los resultados numéricos, tablas CSV y registros se separan por aplicación
en `resultados/cadenas_de_ganancias/` y `resultados/potencias_y_elasticidad/`.
El registro de ejecución identifica el runtime y el hash del cuaderno
ejecutado. Consulta [los resultados](docs/resultados.md),
[el entorno](docs/entorno.md) y
[las fuentes y su alcance](docs/fuentes.md).

## Lectura y reutilización por agentes

El [índice por conceptos](docs/indice.md) orienta a Alphy y a otros
agentes hacia definiciones, ejemplos, evidencia y límites. El catálogo
[sources.json](sources.json) permite localizar esas fuentes sin confundir
referencias primarias con notas y demostraciones originales.

## Estado editorial

Este es el repositorio [JulTob/--Calculus](https://github.com/JulTob/--Calculus).
Los dos casos son demostraciones didácticas reproducibles; todavía no
hay datos empíricos que validen una aplicación concreta. Las ampliaciones
y posibles entradas de wiki se preparan para revisión de Julio, siguiendo
el [proceso de propuesta](docs/indice.md#proponer-contenido-reutilizable).

No se ha probado una sesión Colab en vivo. No se ha elegido licencia ni
se distribuye el texto completo del libro. El manifiesto describe una
instantánea de archivos; véase [cómo mantenerla](docs/entorno.md#instantáneas-y-registros).
