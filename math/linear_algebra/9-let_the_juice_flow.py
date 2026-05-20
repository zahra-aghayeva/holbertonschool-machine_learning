#!/usr/bin/env python3
"""Module utilizing NumPy functions to execute standard array dot products.

Leverages optimized C-backends to handle matrix math multiplication efficiently.
"""
import numpy as np


def np_elementwise_product(mat1, mat2):
    """Computes the algebraic dot product of two arrays via NumPy.

    Args:
        mat1 (np.ndarray or list): First structural numerical matrix.
        mat2 (np.ndarray or list): Second structural numerical matrix.

    Returns:
        np.ndarray: Matrix product configuration, or None if shapes clash.
    """
    try:
        return np.dot(mat1, mat2)
    except ValueError:
        return None
