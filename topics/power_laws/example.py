"""Runnable companion generated from notebook.ipynb.

Edit the notebook, then run maintenance/export_examples.py.
See README.md and references.md for assumptions and source scope.
"""


# Notebook code cell 1.
import csv
import json
import math
import platform
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
A = 3.0
b = 1.5
X = [0.5, 1.0, 2.0, 4.0, 8.0]
Y = [A * value ** b for value in X]
t = [math.log(value) for value in X]
v = [math.log(value) for value in Y]

power_rows = [
    [f"{x:.3f}", f"{y:.6f}", f"{tx:.6f}", f"{vy:.6f}"]
    for x, y, tx, vy in zip(X, Y, t, v)
    ]
print_table(
        "From curve to straight line",
        ["X", "Y", "log(X)", "log(Y)"],
        power_rows,
    )
export_table(
        "power_coordinates.csv",
        ["X", "Y", "log_X", "log_Y"],
        power_rows,
    )

for tx, vy in zip(t, v):
    assert math.isclose(vy, math.log(A) + b * tx, abs_tol=1e-12)


# Notebook code cell 5.
def fit_line(abscissae, ordinates):
    """Fit an intercept and slope to finite, non-degenerate data."""
    if len(abscissae) != len(ordinates) or len(abscissae) < 2:
        raise ValueError(
                "Lists must have equal lengths and contain at least two values."
                )
    if not all(math.isfinite(value) for value in [*abscissae, *ordinates]):
        raise ValueError("Fit data must be finite.")
    mean_x = math.fsum(abscissae) / len(abscissae)
    mean_y = math.fsum(ordinates) / len(ordinates)
    x_differences = [value - mean_x for value in abscissae]
    denominator = math.fsum(value * value for value in x_differences)
    if denominator == 0.0:
        raise ValueError("The input must vary to identify the slope.")
    numerator = math.fsum(
            difference * (value - mean_y)
            for difference, value in zip(x_differences, ordinates)
            )
    slope = numerator / denominator
    return mean_y - slope * mean_x, slope


# Notebook code cell 6.
a_estimated, b_estimated = fit_line(t, v)
A_estimated = math.exp(a_estimated)
print(f"Estimated A = {A_estimated:.9f}; estimated b = {b_estimated:.9f}")
print(f"Alpha derivative = exp(b) = {math.exp(b_estimated):.9f}")

assert math.isclose(A_estimated, A, rel_tol=1e-12)
assert math.isclose(b_estimated, b, abs_tol=1e-12)

# Another input reference: X_new = x / (10*x0).
t_other_reference = [math.log(value / 10.0) for value in X]
a_other, b_other = fit_line(t_other_reference, v)
assert math.isclose(b_other, b, abs_tol=1e-12)
assert math.isclose(
        a_other,
        math.log(A) + b * math.log(10.0),
        abs_tol=1e-12,
    )
print("Changing the reference preserves b and shifts the intercept.")


# Notebook code cell 7.
change_factor = 1.01
exact_change = change_factor ** b - 1.0
linear_change = b * (change_factor - 1.0)
secant_elasticity = math.log(change_factor ** b) / math.log(change_factor)

print_table(
        "Input +1% with b = 1.5",
        ["Quantity", "Value"],
        [
            ["Response: exact change", f"{100 * exact_change:.6f}%"],
            ["Local approximation", f"{100 * linear_change:.6f}%"],
            ["Exact logarithmic ratio", f"{secant_elasticity:.9f}"],
            ],
        )
assert math.isclose(secant_elasticity, b, rel_tol=1e-12)


# Notebook code cell 8.
t_demo = [-2.0, -1.0, 0.0, 1.0, 2.0]
chosen_errors = [0.15, -0.10, 0.05, 0.20, -0.05]
X_demo = [math.exp(value) for value in t_demo]
Y_demo = [
    A * x ** b * math.exp(error)
    for x, error in zip(X_demo, chosen_errors)
    ]
v_demo = [math.log(value) for value in Y_demo]
a_demo, b_demo = fit_line(t_demo, v_demo)

fit_rows = [
    [
        f"{x:.4f}",
        f"{y:.5f}",
        f"{error:+.2f}",
        f"{math.exp(a_demo) * x ** b_demo:.5f}",
        ]
    for x, y, error in zip(X_demo, Y_demo, chosen_errors)
    ]
print_table(
        "Demonstration with fixed errors",
        ["X", "Observed Y", "Log error", "Fitted curve"],
        fit_rows,
        )
export_table(
        "power_fit.csv",
        ["X", "Y", "log_error", "fitted_curve"],
        fit_rows,
        )
print(f"Fitted A = {math.exp(a_demo):.6f}; fitted b = {b_demo:.6f}")
assert math.isclose(a_demo, math.log(A) + 0.05, abs_tol=1e-12)
assert math.isclose(b_demo, 1.49, abs_tol=1e-12)


# Notebook code cell 9.
observations = [1.0, 2.0, 9.0]
original_fit = math.fsum(observations) / len(observations)
mean_log = math.fsum(math.log(y) for y in observations) / len(observations)
log_fit = math.exp(mean_log)

criterion_rows = []
for name, fit in [
        ("Original LS", original_fit),
        ("Log LS", log_fit),
    ]:
    sse_original = math.fsum((y - fit) ** 2 for y in observations)
    sse_log = math.fsum(
            (math.log(y) - math.log(fit)) ** 2
            for y in observations
        )
    criterion_rows.append(
            [
                name,
                f"{fit:.6f}",
                f"{sse_original:.6f}",
                f"{sse_log:.6f}",
                ]
            )

print_table(
        "Same data, different objective",
        ["Fit", "Prediction", "Original SSE", "Log SSE"],
        criterion_rows,
        )
export_table(
        "power_criteria.csv",
        ["fit", "prediction", "sse_original", "sse_log"],
        criterion_rows,
        )
assert original_fit == 4.0
assert math.isclose(log_fit, 18.0 ** (1.0 / 3.0), rel_tol=1e-12)


# Notebook code cell 10.
mean_rows = [
    [f"{sigma:.1f}", f"{A:.6f}", f"{A * math.exp(sigma ** 2 / 2):.6f}"]
    for sigma in [0.0, 0.3, 0.6, 1.0]
    ]
print_table(
        "At X = 1, A = 3: lognormal model",
        ["sigma", "Median", "Mean"],
        mean_rows,
    )
export_table(
        "power_mean_median.csv",
        ["sigma", "median", "mean"],
        mean_rows,
    )
assert math.exp(0.6 ** 2 / 2) > 1.0


# Notebook code cell 11.
additive_responses = [A + error for error in [-4.0, 0.0, 4.0]]
print("Responses with additive error:", additive_responses)

try:
    [positive_log(y) for y in additive_responses]
except ValueError as error:
    print("Domain correctly rejected:", error)
else:
    raise AssertionError("The negative response should have been rejected.")


# Notebook code cell 12.
b_exercise = 0.5
print(f"Factor when doubling X: {2.0 ** b_exercise:.9f}")
print(f"Elasticity: {b_exercise}")
print(f"Alpha derivative: {math.exp(b_exercise):.9f}")
assert math.isclose(2.0 ** b_exercise, math.sqrt(2.0), rel_tol=1e-12)


# Notebook code cell 13.
summary = {
    "status": "passed",
    "application": "power_laws_and_elasticity",
    "python": platform.python_version(),
    "A_noiseless": A_estimated,
    "b_noiseless": b_estimated,
    "A_fixed_errors": math.exp(a_demo),
    "b_fixed_errors": b_demo,
    "original_criterion": original_fit,
    "log_criterion": log_fit,
    "negative_domain_rejected": True,
    "empirical_model_validated": False,
    }
(RESULTS / "checks.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        )
print("Checks passed. CSV files and summary in:", RESULTS)
