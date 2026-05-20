#!/usr/bin/env python3
"""Module for structural concatenation of 2D matrices along specific axes.

Provides methods to merge nested data sequences safely without modifying
the source datasets.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specified axis (0 or 1).

    Args:
        mat1 (list of lists): The primary matrix structural grid.
        mat2 (list of lists): The secondary matrix structural grid.
        axis (int): Axis along which concatenation happens (default: 0).

    Returns:
        list of lists: A combined structural matrix, or None if invalid.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]

    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    return None
