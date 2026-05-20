#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 11, 5, 14, 22], [3, 7, 15, 6, 12, 19]]
the_middle = []
the_middle = [row[2:4] for row in matrix]
print("The middle columns of the matrix are: {}".format(the_middle))
