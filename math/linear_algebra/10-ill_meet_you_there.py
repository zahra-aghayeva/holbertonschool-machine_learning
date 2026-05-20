#!/usr/bin/env python3
"""Module for implementing optimized matrix addition workflows with NumPy.

Performs element-wise summation across array structures safely.
"""
import numpy as np


def np_add(mat1, mat2):
    """Adds two matrices element-by-element using NumPy routines.

    Args:
        mat1 (np.ndarray or list): First input matrix grid.
        mat2 (np.ndarray or list): Second input matrix grid.

    Returns:
        np.ndarray: A new array containing the sum, or None if shapes clash.
    """
    try:
        return np.add(mat1, mat2)
    except ValueError:
        return None
