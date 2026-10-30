"""Export each tutorial's Python cells without duplicating maintained code."""

from pathlib import Path
import argparse
import json


TOPICS = ("gain_chains", "power_laws")


def export_source(notebook_path):
    """Keep code cells unchanged except for the script's output location."""
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
        ]
    output_assignment = 'RESULTS = Path("results")'
    if sum(cell.count(output_assignment) for cell in cells) != 1:
        raise ValueError("Expected one notebook output-directory assignment.")

    cells = [
        cell.replace(
            output_assignment,
            'RESULTS = Path(__file__).resolve().parent / "results"',
            )
        for cell in cells
        ]
    heading = (
        '"""Runnable companion generated from notebook.ipynb.\n\n'
        "Edit the notebook, then run maintenance/export_examples.py.\n"
        "See README.md and references.md for assumptions and source scope.\n"
        '"""\n'
        )
    sections = [
        f"\n\n# Notebook code cell {number}.\n{cell.rstrip()}\n"
        for number, cell in enumerate(cells, start=1)
        ]
    return heading + "".join(sections)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check committed companions without changing files.",
        )
    check = parser.parse_args().check
    root = Path(__file__).resolve().parents[1]

    for name in TOPICS:
        topic = root / "topics" / name
        source = export_source(topic / "notebook.ipynb")
        destination = topic / "example.py"

        if check:
            if not destination.exists() or destination.read_text(
                    encoding="utf-8",
                    ) != source:
                raise SystemExit(f"Regenerate {destination.relative_to(root)}.")
        else:
            destination.write_text(source, encoding="utf-8")

        print(f"{'Checked' if check else 'Exported'} {destination.relative_to(root)}")


if __name__ == "__main__":
    main()
