# Entorno y reproducción

Cada tutorial usa exclusivamente la biblioteca estándar de Python 3.10+.
No requiere GPU, credenciales, red, ficheros privados ni el PDF del libro.
Las tablas se muestran como texto alineado y se exportan a CSV para poder
consultarlas o graficarlas en otra herramienta. No se precisa NumPy,
Matplotlib ni una implementación propia de gráficos.

## Comprobación local

```sh
python3 -B scripts/ejecutar_notebook.py
```

El ejecutor trabaja desde la raíz de esta carpeta y ejecuta ambos cuadernos,
cada uno en un proceso separado. También acepta `ganancias` o `potencias`
como argumento para ejecutar sólo el seleccionado. Cada proceso abre un
espacio de nombres nuevo y ejecuta las celdas de código en orden. Captura
`stdout` y `stderr`, conserva el número de ejecución y detiene el proceso
si una celda falla. No fabrica salidas ni reutiliza el estado de otra
sesión. El registro se guarda dentro de `resultados/<aplicación>/`.

Esta comprobación valida el Python y las aserciones de cada cuaderno. No
comprueba la interfaz de Colab ni las extensiones de Jupyter. La lectura
del cuaderno con salidas guardadas no equivale a una ejecución nueva.

## Reproducción interactiva

Elige un `.ipynb`, ábrelo en Jupyter o súbelo solo a Colab y ejecuta todas
sus celdas desde un runtime nuevo. El código crea su subcarpeta dentro
de `resultados/`, en el directorio actual. En Colab esos ficheros pertenecen
al runtime temporal; descarga los que quieras conservar. Ningún cuaderno
monta Drive ni necesita archivos del otro.

Ambos cuadernos se han ejecutado completamente con CPython 3.14.3 y
3.12.14 en macOS arm64. También se probó cada `.ipynb` por separado,
copiando sólo ese archivo a un directorio vacío y ejecutando sus celdas en
un proceso nuevo. Los registros se separan en `resultados/`. No se ha
realizado una sesión Colab ni validado su interfaz.

## Dependencias

`requirements.txt` no añade paquetes al runtime. Para usar una interfaz
Jupyter local, puedes instalarla en tu propio entorno por separado.
Los paquetes de una interfaz no son dependencias matemáticas del ejemplo.

## Instantáneas y registros

`manifest.json` contiene hashes SHA-256 de una instantánea revisada del
repositorio, excluyendo el propio manifiesto. No es un registro dinámico.
El ejecutor actualiza el cuaderno ejecutado, sus tablas,
`comprobaciones.json` y `ejecucion.json`; no reescribe `manifest.json` ni
los registros históricos `ejecucion-python312.json`,
`ejecucion-python314.json`, `independencia.json`,
`estructura-portabilidad.json` o `portabilidad-zip.json`.

Esos registros históricos describen la preparación original, incluido un
ensayo de un ZIP que no se distribuye aquí. Sus hashes identifican las
instantáneas ensayadas. La ejecución en 3.12 puede producir un hash distinto
porque el cuaderno conserva la versión de Python en su salida. No trates
esos hashes como prueba automática del estado actual de un archivo.

Para comprobar sin modificar esta instantánea, ejecuta desde una copia
temporal de la carpeta. Si se cambia el contenido que se quiere conservar:

1. Ejecuta desde cero y revisa las salidas y sus aserciones.
2. Actualiza la documentación que dependa del resultado. Conserva los
   registros históricos como tales, o repite explícitamente sus pruebas.
3. Regenera los hashes de `manifest.json` para los archivos revisados y
   comprueba que cada ruta y hash coincide antes de proponer el cambio.

El catálogo `sources.json` orienta por conceptos y procedencia; no es un
manifiesto de integridad ni afirma que una referencia externa esté incluida.
