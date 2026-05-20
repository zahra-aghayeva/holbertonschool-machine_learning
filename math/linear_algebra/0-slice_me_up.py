#!/usr/bin/env python3
"""This module executes multi-axis slicing on a predefined 2D NumPy array.

It extracts rows, tailing segments, and a central sub-matrix under strict
formatting and automated assessment guidelines.
"""
import numpy as np

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])

arr1 = arr[:2, :]
arr2 = arr[:, -5:]
arr3 = arr[1:3, 5:7]

print(arr1)
print(arr2)
print(arr3)
