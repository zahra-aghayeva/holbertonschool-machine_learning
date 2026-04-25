#!/usr/bin/env python3
"""
Summation of i squared module
"""


def summation_i_squared(n):
    """
    Calculates the sum of i squared from 1 to n using the formula:
    [n(n+1)(2n+1)] / 6
    """
    if not isinstance(n, int):
        return None
    if n < 0:
        return None
    
    # n = 0 olduqda dövr baş vermir, cəm 0-dır.
    # Düstur n=0 üçün də 0 verir: (0 * 1 * 1) // 6 = 0
    return (n * (n + 1) * (2 * n + 1)) // 6

