import math
import random
import unittest

from parallel_resistance import NumericalStateError, ParallelResistanceBank


def recompute(resistances):
    return 1.0 / math.fsum(1.0 / value for value in resistances)


class ParallelResistanceTests(unittest.TestCase):
    def assert_unchanged_after(self, bank, exception, index, resistance):
        before = (
            bank.snapshot(),
            bank.total_conductance,
            bank.equivalent_resistance,
            )

        with self.assertRaises(exception):
            bank.replace(index, resistance)

        self.assertEqual(
            before,
            (
                bank.snapshot(),
                bank.total_conductance,
                bank.equivalent_resistance,
                ),
            )

    def test_trace_matches_two_known_parallel_resistors(self):
        bank = ParallelResistanceBank([6, 3])
        self.assertEqual(bank.equivalent_resistance, 2)
        trace = bank.replace(0, 3)

        self.assertEqual(bank.snapshot(), (3, 3))
        self.assertEqual(trace.old_conductance, 1 / 6)
        self.assertEqual(trace.new_conductance, 1 / 3)
        self.assertEqual(trace.total_before, 0.5)
        self.assertEqual(trace.total_after, 2 / 3)
        self.assertEqual(trace.equivalent_resistance, 1.5)

    def test_deterministic_updates_match_fresh_fsum(self):
        generator = random.Random(20261029)
        resistances = [10 ** generator.uniform(-2, 2) for _ in range(97)]
        bank = ParallelResistanceBank(resistances)

        for _ in range(2000):
            index = generator.randrange(len(resistances))
            replacement = 10 ** generator.uniform(-2, 2)
            trace = bank.replace(index, replacement)
            resistances[index] = replacement

            self.assertTrue(
                math.isclose(
                    trace.equivalent_resistance,
                    recompute(resistances),
                    rel_tol=2e-13,
                    abs_tol=0,
                    )
                )

    def test_single_branch_avoids_unnecessary_cancellation(self):
        bank = ParallelResistanceBank([1e-100])
        bank.replace(0, 1e100)
        self.assertEqual(bank.equivalent_resistance, 1e100)

    def test_invalid_construction(self):
        cases = (
            ([], ValueError),
            ([0], ValueError),
            ([-1], ValueError),
            ([math.inf], ValueError),
            ([math.nan], ValueError),
            ([True], TypeError),
            (["3"], TypeError),
            ([10 ** 1000], ValueError),
            ([5e-324], NumericalStateError),
            ([1e-308, 1e-308], NumericalStateError),
            )

        for values, exception in cases:
            with self.subTest(values=values):
                with self.assertRaises(exception):
                    ParallelResistanceBank(values)

    def test_invalid_update_preserves_all_state(self):
        bank = ParallelResistanceBank([2, 4])
        cases = (
            (0, 0, ValueError),
            (0, -1, ValueError),
            (0, math.nan, ValueError),
            (0, math.inf, ValueError),
            (0, True, TypeError),
            (0, "3", TypeError),
            (0, 5e-324, NumericalStateError),
            (0, 10 ** 1000, ValueError),
            (-1, 3, IndexError),
            (2, 3, IndexError),
            (True, 3, TypeError),
            (0.0, 3, TypeError),
            )

        for index, value, exception in cases:
            with self.subTest(index=index, value=value):
                self.assert_unchanged_after(bank, exception, index, value)

    def test_total_overflow_update_preserves_state(self):
        bank = ParallelResistanceBank([1e-308, 1])
        self.assert_unchanged_after(bank, NumericalStateError, 1, 1e-308)

    def test_lost_small_branch_is_rejected_instead_of_returning_wrong_value(self):
        bank = ParallelResistanceBank([1e-20, 1])
        self.assert_unchanged_after(bank, NumericalStateError, 0, 1)

        rebuilt = ParallelResistanceBank([1, 1])
        self.assertEqual(rebuilt.equivalent_resistance, 0.5)

    def test_snapshot_cannot_mutate_state(self):
        source = [3, 6]
        bank = ParallelResistanceBank(source)
        source[0] = 99
        self.assertEqual(bank.snapshot(), (3, 6))


if __name__ == "__main__":
    unittest.main(verbosity=2)
