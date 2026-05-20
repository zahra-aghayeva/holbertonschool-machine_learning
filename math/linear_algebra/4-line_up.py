#!/usr/bin/env python3
"""Module for tracking and executing element-wise arithmetic operations.

Combines matching linear sequences mathematically without deep dependencies.
"""


def add_arrays(arr1, arr2):
    """Adds two dimensional lists element by element.

    Args:
        arr1 (list): The first sequence of numbers.
        arr2 (list): The second sequence of numbers.

    Returns:
        list: Summed values, or None if shapes do not match.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
