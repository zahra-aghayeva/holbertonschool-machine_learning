#!/usr/bin/env python3
"""Module focusing on element-by-element array division leveraging NumPy.

Handles rational division calculations across broad coordinate matrices.
"""
import numpy as np


def np_elementwise_divide(mat1, mat2):
    """Divides two matrices element-by-element using NumPy functions.

    Args:
        mat1 (np.ndarray or list): The numerator matrix dataset.
        mat2 (np.ndarray or list): The denominator matrix dataset.

    Returns:
        np.ndarray: Calculated quotients matrix, or None if shapes mismatch.
    """
    try:
        return np.divide(mat1, mat2)
    except ValueError:
        return None
