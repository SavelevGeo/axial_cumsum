from typing import Literal

Axis = Literal['rows', 'columns']

def get_axial_cumsum(array: list[list], axis: Axis) -> list[list]:
    """
    >>> get_axial_cumsum([
    ...     [2, 1, 3, 5, 2],
    ...     [1, 2, 5, 4, 2],
    ...     [4, 1, 2, 0, 3]
    ... ], 'rows')
    [[36, 29, 25, 15, 6], [36, 29, 25, 15, 6], [36, 29, 25, 15, 6]]
    """
    return array

def get_cumsum(array: list[list], axis: Axis) -> list[list]:
    """
    >>> get_cumsum([
    ...     [2, 1, 3, 5, 2],
    ...     [1, 2, 5, 4, 2],
    ...     [4, 1, 2, 0, 3]
    ... ], 'rows')
    [36, 29, 25, 15, 6]
    """
    return array
