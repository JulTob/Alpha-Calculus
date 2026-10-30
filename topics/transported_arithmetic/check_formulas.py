"""Bounded numerical checks for transport formulae and example translations."""

from fractions import Fraction
import json
import math
from pathlib import Path
import platform


def central_difference(
        function,
        value: float,
        step: float = 1e-5,
        ) -> float:
    return (function(value + step) - function(value - step)) / (2 * step)


def simpson_integral(
        function,
        lower: float,
        upper: float,
        panels: int = 2000,
        ) -> float:
    step = (upper - lower) / panels
    weighted = function(lower) + function(upper)
    for index in range(1, panels):
        factor = 4 if index % 2 else 2
        weighted += factor * function(lower + index * step)
    return weighted * step / 3


def inverse_logit(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def logit(value: float) -> float:
    return math.log(value) - math.log1p(-value)


def positive_square(value: float) -> float:
    if value <= 0.0:
        raise ValueError("The declared function domain is (0, infinity).")
    return value**2


results = {}

# For alpha=exp and u(x)=x², the correct pullback is F(t)=2t.
coordinate = 1.0
correct_slope = central_difference(
    lambda value: math.log(positive_square(math.exp(value))),
    coordinate,
    )
correct_alpha_derivative = math.exp(correct_slope)
assert math.isclose(correct_alpha_derivative, math.exp(2), rel_tol=1e-8)
results["correct_exp_square_derivative"] = correct_alpha_derivative

# The inverted composition is not typed for u:(0,infinity)->(0,infinity).
try:
    math.exp(positive_square(math.log(coordinate)))
except ValueError:
    results["inverted_composition_domain_rejected"] = True
else:
    raise AssertionError("The inverted composition evaluated u(0).")

# Only after extending the square to R can the wrong numeric line be tested.
wrong_slope = central_difference(
    lambda value: math.exp(math.log(value)**2),
    coordinate,
    )
wrong_alpha_derivative = math.exp(wrong_slope)
assert math.isclose(wrong_alpha_derivative, 1.0, rel_tol=1e-8)
assert not math.isclose(correct_alpha_derivative, wrong_alpha_derivative)
results["wrong_line_with_explicit_polynomial_extension"] = (
    wrong_alpha_derivative
    )

# Constant elasticity becomes a constant exp-alpha derivative.
power = 1.7
scale = 2.3
power_law_slope = central_difference(
    lambda value: math.log(scale * math.exp(value)**power),
    0.4,
    )
assert math.isclose(power_law_slope, power, rel_tol=1e-8)
results["power_law_exp_alpha_derivative"] = math.exp(power_law_slope)
results["power_law_elasticity"] = power

for value in (-0.4, 0.0, 0.2, 0.5):
    numerical = central_difference(math.atanh, value)
    expected = 1.0 / (1.0 - value**2)
    assert math.isclose(numerical, expected, rel_tol=1e-8)
results["artanh_derivative_values_checked"] = [-0.4, 0.0, 0.2, 0.5]

correct_integral = math.tanh(
    simpson_integral(lambda value: 1.0 / (1.0 - value**2), 0.0, 0.5)
    )
wrong_integral = math.tanh(
    simpson_integral(lambda value: -value / (1.0 - value**2), 0.0, 0.5)
    )
assert math.isclose(correct_integral, 0.5, abs_tol=1e-12)
assert math.isclose(wrong_integral, -1 / 7, abs_tol=1e-12)
results["tanh_integral_correct"] = correct_integral
results["tanh_integral_printed_factor"] = wrong_integral

# For alpha=t³ and u=id, F=id even where alpha inverse is not differentiable.
def real_cube_root(value: float) -> float:
    return math.copysign(abs(value)**(1 / 3), value)


cube_slope = central_difference(
    lambda value: real_cube_root(value**3),
    0.0,
    )
assert math.isclose(cube_slope**3, 1.0, rel_tol=1e-10)
results["cube_generator_identity_derivative_at_zero"] = cube_slope**3
results["cube_inverse_positive_difference_quotients"] = {
    str(step): real_cube_root(step) / step
    for step in (1e-3, 1e-6, 1e-9)
    }

left = Fraction(1, 5)
right = Fraction(3, 10)
transported = left * right / (
    left * right + (1 - left) * (1 - right)
    )
assert transported == Fraction(3, 31)
assert left + right - left * right == Fraction(11, 25)
results["logit_sum_exact"] = str(transported)
results["independent_union_exact"] = str(left + right - left * right)

# The derivative of a response mean w.r.t. a real predictor is ordinary.
beta = 1.7
predictor = 0.3
mean = inverse_logit(-0.8 + beta * predictor)
ordinary_slope = central_difference(
    lambda value: inverse_logit(-0.8 + beta * value),
    predictor,
    )
assert math.isclose(ordinary_slope, beta * mean * (1 - mean), rel_tol=1e-8)
results["logistic_ordinary_response_slope"] = ordinary_slope

# A distinct map on (0,1): u(p)=logistic(logit(p)+c) has F(t)=t+c.
shift = 0.7
point = 0.2
pulled_back_slope = central_difference(
    lambda value: logit(inverse_logit(value + shift)),
    logit(point),
    )
alpha_slope = inverse_logit(pulled_back_slope)
assert math.isclose(alpha_slope, inverse_logit(1.0), rel_tol=1e-8)
results["logit_shift_alpha_derivative"] = alpha_slope

# A cloglog linear shift scales an interval hazard increment, not h itself.
eta = -1.0
shift = 0.8
hazard = -math.expm1(-math.exp(eta))
shifted_hazard = -math.expm1(-math.exp(eta + shift))
increment = -math.log1p(-hazard)
shifted_increment = -math.log1p(-shifted_hazard)
assert math.isclose(shifted_increment / increment, math.exp(shift))
assert not math.isclose(shifted_hazard / hazard, math.exp(shift))
results["cloglog_increment_ratio"] = shifted_increment / increment
results["cloglog_interval_probability_ratio"] = shifted_hazard / hazard

# The log-odds is a difference of surprisals, not their expectation.
probability = 0.8
surprisal_event = -math.log2(probability)
surprisal_complement = -math.log2(1.0 - probability)
odds_bits = math.log2(probability / (1.0 - probability))
entropy_bits = (
    probability * surprisal_event
    + (1.0 - probability) * surprisal_complement
    )
assert math.isclose(odds_bits, surprisal_complement - surprisal_event)
assert math.isclose(odds_bits, logit(probability) / math.log(2.0))
assert math.isclose(odds_bits, 2.0)
assert math.isclose(entropy_bits, 0.7219280948873623)
assert not math.isclose(odds_bits, entropy_bits)
results["shannon_log_odds_bits_at_p_08"] = odds_bits
results["shannon_entropy_bits_at_p_08"] = entropy_bits
results["shannon_event_surprisal_bits_at_p_08"] = surprisal_event
results["shannon_complement_surprisal_bits_at_p_08"] = (
    surprisal_complement
    )

# The physical reciprocal map transports positive conductance addition.
resistance_one = Fraction(100)
resistance_two = Fraction(200)
parallel = 1 / (1 / resistance_one + 1 / resistance_two)
assert parallel == Fraction(200, 3)
assert parallel == (
    resistance_one * resistance_two / (resistance_one + resistance_two)
    )
results["parallel_resistance_100_200_ohms_exact"] = str(parallel)
results["parallel_conductance_siemens_exact"] = str(
    1 / resistance_one + 1 / resistance_two
    )

# The open circuit is a neutral only in the explicit extended physical domain.
open_conductance = 0.0
parallel_with_open = 1.0 / (1.0 / 100.0 + open_conductance)
assert parallel_with_open == 100.0
results["parallel_open_circuit_neutral_extended_domain"] = parallel_with_open

output = {
    "scope": "Bounded formula and example checks; not full-book validation.",
    "python": platform.python_version(),
    "checks_passed": True,
    "results": results,
    }
target = Path(__file__).resolve().parent / "results" / "formula-results.json"
target.parent.mkdir(exist_ok=True)
target.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
