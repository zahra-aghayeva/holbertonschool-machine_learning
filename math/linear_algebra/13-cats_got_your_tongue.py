#!/usr/bin/env python3
"""Module focusing on multi-dimensional array concatenation using NumPy.

Leverages efficient matrix operations to bind structural axes seamlessly.
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two arrays along a specified axis via NumPy routines.

    Args:
        mat1 (np.ndarray or list): First numerical input dataset.
        mat2 (np.ndarray or list): Second numerical input dataset.
        axis (int): Structural dimension along which data is bound (default: 0).

    Returns:
        np.ndarray: The resulting combined array matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
