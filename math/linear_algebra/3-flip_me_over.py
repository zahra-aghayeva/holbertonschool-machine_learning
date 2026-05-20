#!/usr/bin/env python3
"""Module designed for conducting basic matrix transposition operations.

Rearranges row elements into structural column equivalents cleanly.
"""


def matrix_transpose(matrix):
    """Transposes a 2D matrix by converting rows into columns.

    Args:
        matrix (list of lists): The target two-dimensional structure.

    Returns:
        list of lists: The newly transposed matrix view.
    """
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
