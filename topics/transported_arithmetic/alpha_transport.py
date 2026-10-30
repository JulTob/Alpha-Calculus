"""Small, explicit arithmetic-transport helper; not a statistical model."""

from dataclasses import asdict, dataclass
from enum import Enum
import json
import math


class Generator(Enum):
    IDENTITY = "identity"
    EXP = "exp"
    INVERSE_LOGIT = "inverse_logit"


class Operation(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


class UnrepresentableResult(ArithmeticError):
    """The real result lies outside this helper's finite-float encoding."""

    def __init__(
            self,
            generator: Generator,
            coordinate: float,
            ) -> None:
        self.generator = generator
        self.coordinate = coordinate
        super().__init__(
            f"{generator.value}: coordinate {coordinate!r} cannot be "
            "represented inside the generator's image as a finite float."
            )


@dataclass(frozen=True)
class OperationTrace:
    generator: str
    operation: str
    left: float
    right: float
    left_coordinate: float
    right_coordinate: float
    result_coordinate: float
    result: float


def _finite_real(
        value: float,
        label: str,
        ) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} must be an int or float, excluding bool.")

    try:
        converted = float(value)
    except OverflowError as error:
        raise ValueError(f"{label} must be a finite float.") from error

    if not math.isfinite(converted):
        raise ValueError(f"{label} must be finite.")

    return converted


def _coordinate(
        generator: Generator,
        value: float,
        ) -> float:
    if generator is Generator.IDENTITY:
        return value

    if generator is Generator.EXP:
        if value <= 0.0:
            raise ValueError("exp inputs must lie in (0, infinity).")
        return math.log(value)

    if not 0.0 < value < 1.0:
        raise ValueError("inverse_logit inputs must lie strictly in (0, 1).")

    return math.log(value) - math.log1p(-value)


def _represented_value(
        generator: Generator,
        coordinate: float,
        ) -> float:
    try:
        if generator is Generator.IDENTITY:
            return coordinate

        if generator is Generator.EXP:
            result = math.exp(coordinate)
            if result == 0.0 or not math.isfinite(result):
                raise UnrepresentableResult(generator, coordinate)
            return result

        if coordinate >= 0.0:
            result = 1.0 / (1.0 + math.exp(-coordinate))
        else:
            exponential = math.exp(coordinate)
            result = exponential / (1.0 + exponential)

        if not 0.0 < result < 1.0:
            raise UnrepresentableResult(generator, coordinate)

        return result
    except OverflowError as error:
        raise UnrepresentableResult(generator, coordinate) from error


def _apply_operation(
        operation: Operation,
        left: float,
        right: float,
        ) -> float:
    if operation is Operation.ADD:
        return left + right

    if operation is Operation.SUBTRACT:
        return left - right

    if operation is Operation.MULTIPLY:
        return left * right

    if right == 0.0:
        raise ZeroDivisionError(
            "The divisor is alpha-zero: its ordinary coordinate is zero."
            )

    return left / right


def calculate(
        generator: Generator,
        operation: Operation,
        left: float,
        right: float,
        ) -> OperationTrace:
    """Require finite inputs in alpha's image and a nonzero divisor.

    Return the ordinary coordinates and their transported result.
    Raise on invalid domains, coordinate overflow or image-boundary rounding;
    never clip a probability or silently return an excluded endpoint.
    """
    if not isinstance(generator, Generator):
        raise TypeError("generator must be a supported Generator member.")
    if not isinstance(operation, Operation):
        raise TypeError("operation must be a supported Operation member.")

    left = _finite_real(left, "left")
    right = _finite_real(right, "right")
    left_coordinate = _coordinate(generator, left)
    right_coordinate = _coordinate(generator, right)
    result_coordinate = _apply_operation(
        operation,
        left_coordinate,
        right_coordinate,
        )

    if not math.isfinite(result_coordinate):
        raise UnrepresentableResult(generator, result_coordinate)

    result = _represented_value(generator, result_coordinate)

    return OperationTrace(
        generator.value,
        operation.value,
        left,
        right,
        left_coordinate,
        right_coordinate,
        result_coordinate,
        result,
        )


if __name__ == "__main__":
    examples = (
        calculate(Generator.IDENTITY, Operation.ADD, 2.0, 3.0),
        calculate(Generator.EXP, Operation.ADD, 2.0, 3.0),
        calculate(Generator.INVERSE_LOGIT, Operation.ADD, 0.2, 0.3),
        )
    print(json.dumps([asdict(item) for item in examples], indent=2))
