#!/usr/bin/env python3
"""Defines a function to add two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise if they have the same shape.

    Args:
        mat1 (list): First 2D matrix.
        mat2 (list): Second 2D matrix.

    Returns:
        list: New 2D matrix with sum of elements, or None if shapes differ.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
