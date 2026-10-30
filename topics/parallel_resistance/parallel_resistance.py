"""Incremental parallel resistance in positive, finite float coordinates.

This is a restricted transport of addition through conductance, not an
implementation of the book's complete alpha arithmetic.
"""

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
import math
import sys


class NumericalStateError(ArithmeticError):
    """The requested operation exceeds this floating-point representation."""


@dataclass(frozen=True)
class UpdateTrace:
    index: int
    old_conductance: float
    new_conductance: float
    total_before: float
    total_after: float
    equivalent_resistance: float


def _positive_finite_value(value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("Resistance must be an int or float, excluding bool.")

    try:
        resistance = float(value)
    except OverflowError as error:
        raise ValueError("Resistance is outside the finite float range.") from error

    if not math.isfinite(resistance) or resistance <= 0:
        raise ValueError("Resistance must be strictly positive and finite.")

    return resistance


def _conductance(resistance: float) -> float:
    conductance = 1.0 / resistance

    if not math.isfinite(conductance) or conductance <= 0:
        raise NumericalStateError(
            "The reciprocal resistance is outside the positive float range."
            )

    return conductance


def _sum_conductances(values: Sequence[float]) -> float:
    try:
        total = math.fsum(values)
    except OverflowError as error:
        raise NumericalStateError("The total conductance overflowed.") from error

    if not math.isfinite(total) or total <= 0:
        raise NumericalStateError(
            "The total conductance must remain finite and positive."
            )

    return total


def _equivalent_resistance(total: float) -> float:
    resistance = 1.0 / total

    if not math.isfinite(resistance) or resistance <= 0:
        raise NumericalStateError(
            "The equivalent resistance is outside the positive float range."
            )

    return resistance


class ParallelResistanceBank:
    """Store finite positive resistances and their sum of conductances.

    Precondition: a nonempty collection of finite positive int/float values;
    all reciprocal values and totals must fit the positive float range.
    Units: inputs and equivalent resistance in ohms, conductance in siemens.

    Construction consumes O(n) time and memory. Replacement at a known index
    and equivalent-resistance lookup use O(1) work in the unit-cost float
    model. A snapshot intentionally costs O(n).

    Floating-point totals are approximate. Cancellation-sensitive updates
    fail before mutation; callers may explicitly construct a new bank from
    their intended values, paying O(n). Long sequences can still accumulate
    rounding error and may warrant an explicit fresh construction.
    """

    __slots__ = (
        "_resistances",
        "_conductances",
        "_total",
        "_equivalent",
        )

    def __init__(self, resistances: Iterable[int | float]) -> None:
        values = [_positive_finite_value(value) for value in resistances]

        if not values:
            raise ValueError("A parallel bank needs at least one resistance.")

        conductances = [_conductance(value) for value in values]
        total = _sum_conductances(conductances)
        equivalent = _equivalent_resistance(total)

        self._resistances = values
        self._conductances = conductances
        self._total = total
        self._equivalent = equivalent

    @property
    def total_conductance(self) -> float:
        """Return the cached approximate total in siemens, in O(1)."""
        return self._total

    @property
    def equivalent_resistance(self) -> float:
        """Return the cached positive equivalent in ohms, in O(1)."""
        return self._equivalent

    def snapshot(self) -> tuple[float, ...]:
        """Return a read-only copy of the current resistances, in O(n)."""
        return tuple(self._resistances)

    def replace(
            self,
            index: int,
            resistance: int | float,
            ) -> UpdateTrace:
        """Replace exactly one resistance; return its coordinate trace.

        Precondition: a known integer index in [0, n), and a new resistance
        satisfying construction's scalar conditions. On success, only that
        index changes. Any validation/numerical exception preserves state.

        This method never silently recomputes all n conductances.
        """
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("The index must be an integer, excluding bool.")

        if index < 0 or index >= len(self._resistances):
            raise IndexError("The resistance index is outside this bank.")

        new_resistance = _positive_finite_value(resistance)
        new_conductance = _conductance(new_resistance)
        old_conductance = self._conductances[index]
        total_before = self._total

        if len(self._resistances) == 1:
            total_after = new_conductance
        else:
            total_after = _sum_conductances(
                (
                    total_before,
                    -old_conductance,
                    new_conductance,
                    )
                )
            scale = max(total_before, old_conductance, new_conductance)

            # A rounded cached total may have lost the small branches that
            # become important when a dominant branch is removed.
            if total_after / scale <= math.sqrt(sys.float_info.epsilon):
                raise NumericalStateError(
                    "Cancellation-sensitive update; reconstruct the intended "
                    "bank explicitly before continuing."
                    )

        equivalent = _equivalent_resistance(total_after)
        trace = UpdateTrace(
            index=index,
            old_conductance=old_conductance,
            new_conductance=new_conductance,
            total_before=total_before,
            total_after=total_after,
            equivalent_resistance=equivalent,
            )

        self._resistances[index] = new_resistance
        self._conductances[index] = new_conductance
        self._total = total_after
        self._equivalent = equivalent

        return trace
