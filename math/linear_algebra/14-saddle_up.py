#!/usr/bin/env python3
"""Module optimized for formal matrix-matrix multiplication via NumPy tools.

Implements high-performance matrix transformations using standard operators.
"""
import numpy as np


def np_matmul(mat1, mat2):
    """Multiplies two multi-dimensional matrices using NumPy structures.

    Args:
        mat1 (np.ndarray or list): Left-hand matrix transformation block.
        mat2 (np.ndarray or list): Right-hand matrix transformation block.

    Returns:
        np.ndarray: The computed algebraic matrix product.
    """
    return mat1 @ mat2
