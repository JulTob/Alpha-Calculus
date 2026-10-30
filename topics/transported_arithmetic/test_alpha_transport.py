"""Reference examples and meaningful boundaries for alpha_transport."""

from fractions import Fraction
import math
import unittest

from alpha_transport import (
    Generator,
    Operation,
    UnrepresentableResult,
    calculate,
    )


class TransportTests(unittest.TestCase):
    def test_identity_operations(self) -> None:
        for operation, expected in (
            (Operation.ADD, 5.0),
            (Operation.SUBTRACT, -1.0),
            (Operation.MULTIPLY, 6.0),
            (Operation.DIVIDE, 2.0 / 3.0),
            ):
            with self.subTest(operation=operation):
                trace = calculate(Generator.IDENTITY, operation, 2.0, 3.0)
                self.assertAlmostEqual(trace.result, expected)

    def test_exp_sum_is_product(self) -> None:
        trace = calculate(Generator.EXP, Operation.ADD, 2.0, 3.0)
        self.assertAlmostEqual(trace.result, 6.0)
        self.assertAlmostEqual(trace.result_coordinate, math.log(6.0))

    def test_exp_product_is_not_ordinary_product(self) -> None:
        trace = calculate(
            Generator.EXP,
            Operation.MULTIPLY,
            math.e,
            math.e**2,
            )
        self.assertAlmostEqual(trace.result, math.e**2)
        self.assertAlmostEqual(trace.result_coordinate, 2.0)

    def test_logit_sum_has_exact_reference(self) -> None:
        left = Fraction(1, 5)
        right = Fraction(3, 10)
        exact = left * right / (
            left * right + (1 - left) * (1 - right)
            )
        self.assertEqual(exact, Fraction(3, 31))
        trace = calculate(
            Generator.INVERSE_LOGIT,
            Operation.ADD,
            float(left),
            float(right),
            )
        self.assertAlmostEqual(trace.result, float(exact))
        self.assertNotAlmostEqual(trace.result, 0.44)
        self.assertNotAlmostEqual(trace.result, 0.06)

    def test_additive_neutrals(self) -> None:
        for generator, zero, value in (
            (Generator.IDENTITY, 0.0, 0.2),
            (Generator.EXP, 1.0, 2.0),
            (Generator.INVERSE_LOGIT, 0.5, 0.2),
            ):
            with self.subTest(generator=generator):
                trace = calculate(generator, Operation.ADD, value, zero)
                self.assertAlmostEqual(trace.result, value)

    def test_multiplicative_neutrals(self) -> None:
        for generator, one, value in (
            (Generator.IDENTITY, 1.0, 0.2),
            (Generator.EXP, math.e, 2.0),
            (Generator.INVERSE_LOGIT, 1.0 / (1.0 + math.exp(-1)), 0.2),
            ):
            with self.subTest(generator=generator):
                trace = calculate(generator, Operation.MULTIPLY, value, one)
                self.assertAlmostEqual(trace.result, value)

    def test_divisor_is_alpha_zero(self) -> None:
        for generator, zero, value in (
            (Generator.IDENTITY, 0.0, 2.0),
            (Generator.EXP, 1.0, 2.0),
            (Generator.INVERSE_LOGIT, 0.5, 0.2),
            ):
            with self.subTest(generator=generator):
                with self.assertRaisesRegex(ZeroDivisionError, "alpha-zero"):
                    calculate(generator, Operation.DIVIDE, value, zero)

    def test_input_domains(self) -> None:
        for generator, invalid in (
            (Generator.EXP, 0.0),
            (Generator.EXP, -1.0),
            (Generator.INVERSE_LOGIT, 0.0),
            (Generator.INVERSE_LOGIT, 1.0),
            (Generator.INVERSE_LOGIT, 1.1),
            (Generator.INVERSE_LOGIT, -0.1),
            ):
            with self.subTest(generator=generator, invalid=invalid):
                with self.assertRaises(ValueError):
                    calculate(generator, Operation.ADD, invalid, 0.5)

    def test_types_and_nonfinite_inputs(self) -> None:
        for invalid in (True, None, "0.2", [0.2]):
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    calculate(Generator.IDENTITY, Operation.ADD, invalid, 1.0)

        for invalid in (math.nan, math.inf, -math.inf, 10**1000):
            with self.subTest(invalid=str(invalid)):
                with self.assertRaises(ValueError):
                    calculate(Generator.IDENTITY, Operation.ADD, invalid, 1.0)

    def test_unsupported_generator_or_operation(self) -> None:
        with self.assertRaises(TypeError):
            calculate("exp", Operation.ADD, 1.0, 2.0)
        with self.assertRaises(TypeError):
            calculate(Generator.IDENTITY, "add", 1.0, 2.0)

    def test_coordinate_overflow(self) -> None:
        with self.assertRaises(UnrepresentableResult):
            calculate(Generator.IDENTITY, Operation.MULTIPLY, 1e308, 1e308)

    def test_exp_output_overflow_keeps_coordinate(self) -> None:
        with self.assertRaises(UnrepresentableResult) as result:
            calculate(Generator.EXP, Operation.ADD, 1e308, 1e308)
        self.assertTrue(math.isfinite(result.exception.coordinate))
        self.assertGreater(result.exception.coordinate, 1000.0)

    def test_exp_output_underflow_is_explicit(self) -> None:
        with self.assertRaises(UnrepresentableResult):
            calculate(Generator.EXP, Operation.ADD, 1e-300, 1e-300)

    def test_logit_boundary_rounding_is_explicit(self) -> None:
        high = math.nextafter(1.0, 0.0)
        with self.assertRaises(UnrepresentableResult) as result:
            calculate(Generator.INVERSE_LOGIT, Operation.ADD, high, high)
        self.assertTrue(math.isfinite(result.exception.coordinate))


if __name__ == "__main__":
    unittest.main(verbosity=2)
