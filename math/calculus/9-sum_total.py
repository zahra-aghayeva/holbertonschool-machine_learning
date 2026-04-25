#!/usr/bin/env python3
"""
Module for calculating the sum of squares
"""


def summation_i_squared(n):
    """
    Calculates the sum of i^2 from 1 to n
    Args:
        n: the stopping condition
    Returns:
        The integer value of the sum, or None if n is not valid
    """
    if not isinstance(n, int) or n < 0:
        return None
    
    # n=0 olduqda cəm 0-dır. Düstur bunu zatən hesablayır.
    return (n * (n + 1) * (2 * n + 1)) // 6
