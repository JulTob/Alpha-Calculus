import math
from dataclasses import dataclass

@dataclass(frozen=True)
class AlphaStructure:
    name: str
    generator: object
    inverse: object

    def __call__(structure, value: float):
        """Exp(value) -> Maps a real-world value into the Alpha space"""
        return AlphaElement(structure, structure.inverse(value))

    def __matmul__(structure, coordinate: float):
        """Structure @ coordinate -> Creates AlphaElement directly from coordinate"""
        return AlphaElement(structure, coordinate)

    def __getitem__(structure, coordinate: float):
        """Structure[coordinate] -> Alternative lookup-style syntax"""
        return AlphaElement(structure, coordinate)

@dataclass(frozen=True)
class AlphaElement:
    structure: AlphaStructure
    coordinate: float

    @property
    def value(element):
        return element.structure.generator(element.coordinate)

    def __repr__(element):
        """Customize how the element displays when typed directly as `x`"""
        return f"{element.structure.name}⟨val: {element.value:.4f}, coord: {element.coordinate:.4f}⟩"

    def __call__(element, new_value=None):
        """
        x() -> Returns the current real-world value.
        x(new_value) -> Returns a new AlphaElement updated to the given real-world value.
        """
        if new_value is None:
            return element.value
        return element.structure(new_value)

    def __getitem__(element, key):
        """
        x[:] -> Returns the coordinate.
        x[new_coordinate] -> Returns a new AlphaElement updated to that coordinate (e.g., x[0] updates coordinate to 0).
        """
        # If key is an empty slice (i.e., x[:]) or None/empty tuple/Ellipsis, return the coordinate.
        if isinstance(key, slice) and key.start is None and key.stop is None and key.step is None:
            return element.coordinate
        if key is Ellipsis or key is None or key == ():
            return element.coordinate

        # Otherwise, treat it as an update returning a new AlphaElement with the new coordinate.
        return element.structure @ key

    def __add__(element, other):
        if element.structure is not other.structure:
            raise TypeError("different structures")
        return element.structure @ (element.coordinate + other.coordinate)

    def __sub__(element, other):
        if element.structure is not other.structure:
            raise TypeError("different structures")
        return element.structure @ (element.coordinate - other.coordinate)

    def __mul__(element, other):
        if element.structure is not other.structure:
            raise TypeError("different structures")
        return element.structure @ (element.coordinate * other.coordinate)

    def __truediv__(element, other):
        if element.structure is not other.structure:
            raise TypeError("different structures")
        if other.coordinate == 0:
            raise ZeroDivisionError("alpha zero")
        return element.structure @ (element.coordinate / other.coordinate)

    def __abs__(element):
        """abs(x) -> Returns a new AlphaElement with the absolute value of the coordinate"""
        return element.structure @ abs(element.coordinate)
