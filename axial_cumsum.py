import numpy as np

from typing import Literal, Any
from numpy.typing import NDArray

Axis = Literal["rows", "columns"]


def get_axial_cumsum(
    array: list[list[Any]] | NDArray[Any], axis: Axis
) -> NDArray[Any]:
    """
    >>> get_axial_cumsum([
    ...     [2, 1, 3, 5, 2],
    ...     [1, 2, 5, 4, 2],
    ...     [4, 1, 2, 0, 3]
    ... ], 'rows')
    [[36, 29, 25, 15, 6], [36, 29, 25, 15, 6], [36, 29, 25, 15, 6]]
    """
    sum_along_axis: NDArray[Any] = np.sum(array, 0 if axis == "rows" else 1)

    return sum_along_axis
