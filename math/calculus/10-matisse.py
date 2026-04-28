#!/usr/bin/env python3
"""
Module for polynomial derivative
"""


def poly_derivative(poly):
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])

    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    return derivative
