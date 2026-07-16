import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    transpose = []

    for j in range(len(A[0])):
        row = []
        for i in range(len(A)):
            row.append(A[i][j])
        transpose.append(row)
    
    return np.array(transpose)
matrix_transpose(A)
