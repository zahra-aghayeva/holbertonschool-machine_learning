#!/usr/bin/env python3
"""Module containing functions to verify structural matrix shapes.

Computes matrix boundaries to validate multi-dimensional arrays.
"""


def matrix_shape(matrix):
    """Scans and extracts the overall geometric shape of a matrix grid.

    Args:
        matrix (list): Nested lists forming the structural matrix.

    Returns:
        list: Numeric shape values representing the axes.
    """
    dimensions = []
    while isinstance(matrix, list):
        dimensions.append(len(matrix))
        if not matrix:
            break
        matrix = matrix[0]
    return dimensions
