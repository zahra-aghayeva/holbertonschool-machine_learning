#!/usr/bin/env python3
"""This module provides a function to retrieve the shape of a matrix.

It inspects the dimensions of a multi-dimensional array using NumPy
and returns its structural configuration.
"""


def slice_me_up(matrix):
    """Calculates and returns the structural dimensions of a given matrix.

    Args:
        matrix (np.ndarray): The input matrix to be analyzed.

    Returns:
        list: A list representing the dimensions (shape) of the matrix.
    """
    return list(matrix.shape)
