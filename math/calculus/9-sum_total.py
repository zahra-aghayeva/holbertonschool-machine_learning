#!/usr/bin/env python3
"""
Summation of i squared module
"""


def summation_i_squared(n):
    """
    Calculates the sum of i squared from 1 to n
    Args:
        n: the stopping condition
    Returns:
        The integer value of the sum, or None if n is invalid
    """
    if not isinstance(n, int) or n < 1:
        if n == 0:
            return 0
        return None
    
    # Formula: [n(n+1)(2n+1)] / 6
    sum_total = (n * (n + 1) * (2 * n + 1)) // 6
    return sum_total

