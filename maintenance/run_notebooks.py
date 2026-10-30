"""Run one or both tutorials from scratch without a Jupyter kernel."""

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


APPLICATIONS = {
    "gains": "gain_chains",
    "power-laws": "power_laws",
    }


def execute_cell(
        cell,
        number,
        namespace,
    ):
    """Capture a real cell and propagate failures after saving its output."""
    output = StringIO()
    code = "".join(cell["source"])
    cell["execution_count"] = number
    cell["outputs"] = []

    try:
        with redirect_stdout(output), redirect_stderr(output):
            exec(
                    compile(code, f"<cell {number}>", "exec"),
                    namespace,
                    )
    except Exception as error:
        cell["outputs"].append(
                {
                    "output_type": "error",
                    "ename": type(error).__name__,
                    "evalue": str(error),
                    "traceback": traceback.format_exception(error),
                    }
                )
        raise
    finally:
        if output.getvalue():
            cell["outputs"].insert(
                    0,
                    {
                        "output_type": "stream",
                        "name": "stdout",
                        "text": output.getvalue().splitlines(keepends=True),
                        },
                    )


def execute_notebook(root, name):
    """Run one application and retain its own execution record and outputs."""
    topic = root / "topics" / name
    path = topic / "notebook.ipynb"
    os.chdir(topic)
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
    namespace = {"__name__": "__main__"}
    start = time.perf_counter()
    number = 0
    status = "passed"

    try:
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                number += 1
                execute_cell(cell, number, namespace)
    except Exception:
        status = "failed"
        raise
    finally:
        path.write_text(
                json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
                )
        record = {
            "status": status,
            "application": name,
            "notebook": str(path.relative_to(root)),
            "utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "code_cells_executed": number,
            "elapsed_seconds": time.perf_counter() - start,
            "notebook_sha256": sha256(path.read_bytes()).hexdigest(),
            "mode": "Sequential Python exec in a fresh namespace; no Jupyter kernel.",
            "colab_live_execution": False,
            }
        destination = topic / "results" / "execution.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
                json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                )
        print(json.dumps(record, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(
            description="Run one application or both in separate processes.",
            )
    parser.add_argument(
            "application",
            nargs="?",
            choices=[*APPLICATIONS, "all"],
            default="all",
            )
    option = parser.parse_args().application
    if option == "all":
        for name in APPLICATIONS:
            subprocess.run(
                    [sys.executable, "-B", str(Path(__file__).resolve()), name],
                    check=True,
                    )
        return

    root = Path(__file__).resolve().parents[1]
    execute_notebook(root, APPLICATIONS[option])


if __name__ == "__main__":
    main()
