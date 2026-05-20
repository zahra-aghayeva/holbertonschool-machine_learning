#!/usr/bin/env python3
"""Module focused on expanding arrays via basic scalar scaling mechanisms.

Multiplies sequence elements systematically by a uniform numeric variable.
"""


def multiply_elementwise(matrix, alpha):
    """Multiplies each numerical element in an array by a scalar factor.

    Args:
        matrix (list): The original array structure.
        alpha (int/float): The scaling factor.

    Returns:
        list: A newly scaled array representation.
    """
    return [element * alpha for element in matrix]
