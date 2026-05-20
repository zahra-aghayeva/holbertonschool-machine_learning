#!/usr/bin/env python3
"""Slice a 2D array."""
import numpy as np
arr = np.arange(1, 31).reshape(3, 10)
arr1, arr2, arr3 = arr[:2, :], arr[:, -5:], arr[1:3, 5:7]
print(arr1)
print(arr2)
print(arr3)
