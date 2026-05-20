#!/usr/bin/env python3
"""Defines element-wise operations on numpy ndarrays."""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction,
    multiplication, and division.

    Args:
        mat1 (numpy.ndarray): The first matrix or scalar.
        mat2 (numpy.ndarray): The second matrix or scalar.

    Returns:
        tuple: A tuple containing the sum, difference, product,
               and quotient matrices respectively.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
