"""Ejecuta uno o todos los tutoriales desde cero, sin un kernel Jupyter."""

from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from hashlib import sha256
from io import StringIO
from pathlib import Path
import argparse
import json
import os
import platform
import subprocess
import sys
import time
import traceback


APLICACIONES = {
    "ganancias": "cadenas_de_ganancias",
    "potencias": "potencias_y_elasticidad",
    }


def ejecutar_celda(celda, numero, espacio):
    """Captura una celda real; propaga sus fallos tras guardar la salida."""
    salida = StringIO()
    codigo = "".join(celda["source"])
    celda["execution_count"] = numero
    celda["outputs"] = []

    try:
        with redirect_stdout(salida), redirect_stderr(salida):
            exec(
                    compile(codigo, f"<celda {numero}>", "exec"),
                    espacio,
                    )
    except Exception as error:
        celda["outputs"].append(
                {
                    "output_type": "error",
                    "ename": type(error).__name__,
                    "evalue": str(error),
                    "traceback": traceback.format_exception(error),
                    }
                )
        raise
    finally:
        if salida.getvalue():
            celda["outputs"].insert(
                    0,
                    {
                        "output_type": "stream",
                        "name": "stdout",
                        "text": salida.getvalue().splitlines(keepends=True),
                        },
                    )


def ejecutar_cuaderno(raiz, nombre):
    """Ejecuta una aplicación y conserva su propio registro y sus salidas."""
    ruta = raiz / "notebooks" / f"{nombre}.ipynb"
    os.chdir(raiz)
    cuaderno = json.loads(ruta.read_text(encoding="utf-8"))
    for celda in cuaderno["cells"]:
        if celda["cell_type"] == "code":
            celda["execution_count"] = None
            celda["outputs"] = []
    espacio = {"__name__": "__main__"}
    inicio = time.perf_counter()
    numero = 0
    estado = "passed"

    try:
        for celda in cuaderno["cells"]:
            if celda["cell_type"] == "code":
                numero += 1
                ejecutar_celda(celda, numero, espacio)
    except Exception:
        estado = "failed"
        raise
    finally:
        ruta.write_text(
                json.dumps(cuaderno, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
                )
        registro = {
            "status": estado,
            "application": nombre,
            "notebook": str(ruta.relative_to(raiz)),
            "utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "code_cells_executed": numero,
            "elapsed_seconds": time.perf_counter() - inicio,
            "notebook_sha256": sha256(ruta.read_bytes()).hexdigest(),
            "mode": "Sequential Python exec in a fresh namespace; no Jupyter kernel.",
            "colab_live_execution": False,
            }
        destino = raiz / "resultados" / nombre / "ejecucion.json"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(
                json.dumps(registro, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                )
        print(json.dumps(registro, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(
            description="Ejecuta una aplicación o ambas en procesos separados.",
            )
    parser.add_argument(
            "aplicacion",
            nargs="?",
            choices=[*APLICACIONES, "todos"],
            default="todos",
            )
    opcion = parser.parse_args().aplicacion
    if opcion == "todos":
        for nombre in APLICACIONES:
            subprocess.run(
                    [sys.executable, "-B", str(Path(__file__).resolve()), nombre],
                    check=True,
                    )
        return

    raiz = Path(__file__).resolve().parents[1]
    ejecutar_cuaderno(raiz, APLICACIONES[opcion])


if __name__ == "__main__":
    main()
