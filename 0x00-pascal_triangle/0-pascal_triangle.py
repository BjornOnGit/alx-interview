#!/usr/bin/python3
"""pascal triangle"""

def pascal_triangle(n):
    """
    The function generates a pascal
    triangle where n is the number of rows to be generated.
    Logic: The whole triangle is seen as a super array while
    each row is a sub array in the super array(the triangle)
    """
    super_array = []
    for i in range(0, n):
        sub_array = []
        if len(super_array) != 0:
            prev_arr = super_array[i - 1]
        for j in range(0, i + 1):
            if j == 0 or j == i:
                sub_array.append(1)
            else:
                sub_array.append(prev_arr[j - 1] + prev_arr[j])
        super_array.append(sub_array)
    return super_array
