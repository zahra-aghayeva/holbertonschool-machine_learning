#!/usr/bin/env python3
"""Module focused on determining the nested matrix shape iteratively.

Provides structural analysis of multi-dimensional lists without external tools.
"""


def matrix_shape(matrix):
    """Computes the exact dimensions of a nested list structure.

    Args:
        matrix (list): A nested list representing a matrix.

    Returns:
        list: The size configurations across all dimensions.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
