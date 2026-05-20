#!/usr/bin/env python3
"""Module utilizing NumPy to handle element-wise matrix multiplication.

Computes Hadamard products over matching numerical multidimensional arrays.
"""
import numpy as np


def np_elementwise_multiply(mat1, mat2):
    """Multiplies two matrices element-by-element using NumPy operations.

    Args:
        mat1 (np.ndarray or list): Primary numerical dataset.
        mat2 (np.ndarray or list): Secondary numerical dataset.

    Returns:
        np.ndarray: Calculated elementwise products, or None if invalid.
    """
    try:
        return np.multiply(mat1, mat2)
    except ValueError:
        return None
