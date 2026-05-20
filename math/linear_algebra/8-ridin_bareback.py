#!/usr/bin/env python3
"""Module optimized for custom matrix-matrix mathematical multiplication.

Executes algebraic inner dot-products over multi-dimensional grids.
"""


def mat_mul(mat1, mat2):
    """Multiplies two 2D matrices matching structural vector dimensions.

    Args:
        mat1 (list of lists): Left-hand matrix transformation block.
        mat2 (list of lists): Right-hand matrix transformation block.

    Returns:
        list of lists: The calculated matrix product, or None if incompatible.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):
        row_result = []
        for j in range(len(mat2[0])):
            element_sum = 0
            for k in range(len(mat2)):
                element_sum += mat1[i][k] * mat2[k][j]
            row_result.append(element_sum)
        result.append(row_result)

    return result
