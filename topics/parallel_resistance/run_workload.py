"""Execute reproducible updates and count actual helper inputs, not timings."""

from dataclasses import asdict
import json
import math
from pathlib import Path
import platform
import random
import sys
from unittest.mock import patch

import parallel_resistance as implementation


def run_case(size: int, updates: int) -> dict:
    generator = random.Random(20261029 + size)
    values = [generator.uniform(10, 1000) for _ in range(size)]
    largest_relative_error = 0.0
    first_trace = None

    with (
        patch.object(
            implementation,
            "_conductance",
            wraps=implementation._conductance,
            ) as conductance_calls,
        patch.object(
            implementation,
            "_sum_conductances",
            wraps=implementation._sum_conductances,
            ) as sum_calls,
        ):
        bank = implementation.ParallelResistanceBank(values)

        for _ in range(updates):
            index = generator.randrange(size)
            replacement = generator.uniform(10, 1000)
            trace = bank.replace(index, replacement)
            values[index] = replacement
            expected = 1.0 / math.fsum(1.0 / value for value in values)
            actual = bank.equivalent_resistance
            relative_error = abs(actual - expected) / expected
            largest_relative_error = max(largest_relative_error, relative_error)

            if first_trace is None:
                first_trace = asdict(trace)

            if not math.isclose(actual, expected, rel_tol=2e-13, abs_tol=0):
                raise AssertionError("The incremental result differs from fresh fsum.")

        conductance_evaluations = conductance_calls.call_count
        sum_input_lengths = [
            len(call.args[0])
            for call in sum_calls.call_args_list
            ]
        fsum_terms = sum(sum_input_lengths)

    if conductance_evaluations != size + updates:
        raise AssertionError("Unexpected conductance evaluation count.")

    if fsum_terms != size + 3 * updates:
        raise AssertionError("An update may be traversing the whole bank.")

    if sum_input_lengths[0] != size or set(sum_input_lengths[1:]) != {3}:
        raise AssertionError("Each incremental update must sum exactly three terms.")

    return {
        "n": size,
        "updates_and_queries": updates,
        "incremental": {
            "conductance_evaluations_including_construction": conductance_evaluations,
            "fsum_terms_including_construction": fsum_terms,
            "update_fsum_terms_each": 3,
            },
        "recompute_each_query": {
            "conductance_evaluations_excluding_initial_validation": size * updates,
            "fsum_terms": size * updates,
            },
        "max_relative_error_against_fresh_fsum": largest_relative_error,
        "first_update_trace": first_trace,
        "final_equivalent_resistance_ohm": bank.equivalent_resistance,
        }


def main() -> None:
    report = {
        "python": sys.version,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "seed_rule": "random.Random(20261029 + n)",
        "workload": (
            "Initialize n independent resistances uniformly in [10, 1000] ohm. "
            "For each of 256 updates, select a known integer index, replace its "
            "resistance with a fresh value in that interval, and query the equivalent."
            ),
        "counts_measure": (
            "Actual production helper calls and lengths of inputs passed to math.fsum. "
            "These are work indicators, not timings or counts of machine instructions."
            ),
        "competent_conventional_baseline": (
            "Maintain the same sum of conductances: O(n) construction, "
            "O(1) update/query, O(n) memory; identical asymptotic performance."
            ),
        "cases": [run_case(size, 256) for size in (8, 128, 2048)],
        }
    destination = (
        Path(__file__).resolve().parent
        / "results"
        / "workload-results.json"
        )
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
