"""Runnable companion generated from notebook.ipynb.

Edit the notebook, then run maintenance/export_examples.py.
See README.md and references.md for assumptions and source scope.
"""


# Notebook code cell 1.
import csv
import json
import math
import platform
import random
from fractions import Fraction
from pathlib import Path

RESULTS = Path(__file__).resolve().parent / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

print("Python:", platform.python_version())
print("Float precision: approximately 16 significant digits.")


# Notebook code cell 2.
def positive_log(value):
    """Coordinate of a positive, finite, dimensionless quantity."""
    if not math.isfinite(value) or value <= 0:
        raise ValueError("The quantity must be positive and finite.")
    return math.log(value)


def product_from_log(total):
    """Recover a positive product representable as a float."""
    if not math.isfinite(total):
        raise ValueError("The logarithmic sum must be finite.")
    product = math.exp(total)
    if product == 0.0:
        raise ArithmeticError("The positive product was rounded to zero.")
    return product


# Notebook code cell 3.
def print_table(
        title,
        header,
        rows,
    ):
    """Print a small table with aligned columns."""
    data = [
        [str(value) for value in row]
        for row in [header, *rows]
        ]
    widths = [
        max(map(len, column))
        for column in zip(*data)
        ]

    print(title)
    for index, row in enumerate(data):
        print(
                " | ".join(
                        value.ljust(width)
                        for value, width in zip(row, widths)
                    )
            )
        if index == 0:
            print("-+-".join("-" * width for width in widths))


def export_table(
        name,
        header,
        rows,
    ):
    """Save table data as UTF-8 CSV."""
    with (RESULTS / name).open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


# Notebook code cell 4.
gains = [2.0, 3.0, 5.0]
coordinates = [positive_log(value) for value in gains]
total_log = math.fsum(coordinates)

stage_rows = [
    [index + 1, gain, f"{coordinate:.9f}"]
    for index, (gain, coordinate)
    in enumerate(zip(gains, coordinates))
    ]
print_table(
        "Contribution by stage",
        ["Stage", "g", "log(g)"],
        stage_rows,
    )
print(f"S = {total_log:.9f}; exp(S) = {math.exp(total_log):.9f}")

assert math.isclose(math.exp(total_log), 30.0, rel_tol=1e-12)
export_table(
        "gain_stages.csv",
        ["stage", "g", "log_g"],
        stage_rows,
    )


# Notebook code cell 5.
index = 1
new_gain = 4.0
new_gains = gains.copy()
new_gains[index] = new_gain

new_total = math.fsum(
        [
            total_log,
            -coordinates[index],
            positive_log(new_gain),
            ]
        )
via_log = product_from_log(new_total)
via_quotient = math.prod(gains) / gains[index] * new_gain
via_recomputation = math.prod(new_gains)

print_table(
        "Three methods, one replacement",
        ["Method", "New product"],
        [
            ["Recompute", f"{via_recomputation:.12g}"],
            ["Product/quotient", f"{via_quotient:.12g}"],
            ["Sum of logarithms", f"{via_log:.12g}"],
            ],
        )
assert math.isclose(via_log, 40.0, rel_tol=1e-12)
assert via_quotient == via_recomputation == 40.0


# Notebook code cell 6.
rng = random.Random(975)
factors = [2.0 ** rng.randint(-3, 3) for _ in range(16)]
logs = [math.log(value) for value in factors]
log_sum = math.fsum(logs)
product_quotient = math.prod(factors)
max_error = 0.0

for _ in range(256):
    position = rng.randrange(len(factors))
    new_value = 2.0 ** rng.randint(-3, 3)
    new_log = math.log(new_value)
    log_sum = math.fsum([log_sum, -logs[position], new_log])
    product_quotient = product_quotient / factors[position] * new_value
    factors[position] = new_value
    logs[position] = new_log
    reference = float(math.prod(Fraction(value) for value in factors))
    computed = product_from_log(log_sum)
    assert product_quotient == reference
    assert math.isclose(computed, reference, rel_tol=1e-12)
    max_error = max(max_error, abs(computed / reference - 1))

print("Replacements checked: 256 / 256")
print(f"Maximum relative error of the log method: {max_error:.3e}")
print("Product/quotient: exact for this powers-of-two workload.")


# Notebook code cell 7.
def describe_return(log_sum):
    try:
        return f"{product_from_log(log_sum):.9g}"
    except OverflowError:
        return "Overflow"
    except ArithmeticError:
        return "Underflow to zero"


range_rows = []
for label, values in [
        ("Large", [1e200, 1e200]),
        ("Small", [1e-200, 1e-200]),
        ("Balanced", [1e200, 1e200, 1e-200, 1e-200]),
        ]:
    range_sum = math.fsum(math.log(value) for value in values)
    range_rows.append(
            [
                label,
                math.prod(values),
                f"{range_sum:.6f}",
                describe_return(range_sum),
                ]
            )

print_table(
        "Representable range",
        ["Case", "Direct product", "S", "exp(S)"],
        range_rows,
        )
export_table(
        "gain_range.csv",
        ["case", "direct", "log_total", "return"],
        range_rows,
        )
print("Product with reordered factors:", math.prod([1e200, 1e-200] * 2))
assert describe_return(0.0) == "1"


# Notebook code cell 8.
small_factor = 1.00000000000001
small_term = math.log(small_factor)
accumulated = math.fsum([700.0, -700.0, small_term])
accumulated = math.fsum([accumulated, -700.0, 0.0])
accumulated = math.fsum([accumulated, 700.0, 0.0])
rebuilt = math.fsum([0.0, 0.0, small_term])

print_table(
        "Cancellation during successive updates",
        ["Method", "Product"],
        [
            ["Expected", f"{small_factor:.17g}"],
            ["Incremental accumulator", f"{math.exp(accumulated):.17g}"],
            ["Reconstruction", f"{math.exp(rebuilt):.17g}"],
            ],
        )
assert accumulated == 0.0
assert math.exp(accumulated) != small_factor
assert math.exp(rebuilt) == small_factor


# Notebook code cell 9.
exercise = [0.5, 2.0, 8.0]
answer_log = math.fsum(
        [
            math.fsum(math.log(value) for value in exercise),
            -math.log(2.0),
            math.log(3.0),
            ]
        )
print("Answer:", math.exp(answer_log))
assert math.isclose(math.exp(answer_log), 12.0, rel_tol=1e-12)


# Notebook code cell 10.
summary = {
    "status": "passed",
    "application": "gain_chains",
    "python": platform.python_version(),
    "replacements": 256,
    "factors": 16,
    "seed": 975,
    "workload": "Powers of two, integer exponents from -3 to 3.",
    "max_log_relative_error": max_error,
    "example_30_to_40": via_log,
    "incremental_cancellation": math.exp(accumulated),
    "rebuilt_cancellation": math.exp(rebuilt),
    }
(RESULTS / "checks.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        )
print("Checks passed. CSV files and summary in:", RESULTS)
