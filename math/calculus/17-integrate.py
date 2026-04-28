#!/usr/bin/env python3
"""
Module to calculate the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int) and not isinstance(C, float):
        return None
    
    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    # İnteqral sabiti C siyahının ilk elementidir (x^0)
    # Tam ədəd olub olmadığını yoxlayırıq
    if isinstance(C, float) and C.is_integer():
        C = int(C)
    
    integral = [C]

    for i in range(len(poly)):
        new_coeff = poly[i] / (i + 1)
        
        # Əgər ədəd .0 ilə bitirsə (məsələn 5.0), onu int edirik
        if new_coeff.is_integer():
            new_coeff = int(new_coeff)
        
        integral.append(new_coeff)

    # Siyahının sonundakı artıq sıfırları təmizləyirik
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
