#!/usr/bin/env python3
"""Defines a function to transpose a matrix using NumPy."""


def np_transpose(matrix):
    """Transposes a numpy.ndarray matrix.

    Args:
        matrix (numpy.ndarray): The matrix to be transposed.

    Returns:
        numpy.ndarray: A new transposed numpy array.
    """
    return matrix.transpose()
