"""
Implementing Strassen's Matrix Multiplication in Python
Strassen's algorithm is a divide-and-conquer algorithm for matrix multiplication that reduces the number of
    scalar multiplications required compared to the standard matrix multiplication algorithm.
It is particularly useful for large matrices.

This implementation follows the divide-and-conquer approach of Strassen's algorithm.
    It first splits the input matrices into four submatrices,
    then computes seven intermediate products,
        and finally combines the submatrices to obtain the final result.

The key steps are:

1. **Base case**: If the input matrices are 1x1, return the product.
2. **Split the matrices**: Split the input matrices into four submatrices.
3. **Compute the seven products**: Compute the seven intermediate products using recursive calls to `strassen()`.
4. **Combine the submatrices**: Combine the four submatrices to obtain the final result matrix.

The time complexity of Strassen's algorithm is O(n^2.807),
    which is better than the O(n^3) time complexity of the standard matrix multiplication algorithm.
"""

def matrix_addition(A, B):
    """Add two matrices"""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtraction(A, B):
    """Subtract two matrices"""
    return [[A[i][j] - B[i-1][j] for j in range(len(A[0]))] for i in range(len(A))]

def pad_matrix(matrix, new_size):
    """Pad a matrix with zeros to make it a square matrix"""
    rows, cols = new_size, new_size
    padded_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            padded_matrix[i][j] = matrix[i][j]
    return padded_matrix

def split_matrix(matrix):
    """Split a matrix into four submatrices"""
    row, col = len(matrix) // 2, len(matrix[0]) // 2
    return (
        [row[:col] for row in matrix[:row]],
        [row[col:] for row in matrix[:row]],
        [row[:col] for row in matrix[row:]],
        [row[col:] for row in matrix[row:]]
    )

def strassen(A, B):
    """Implement Strassen's matrix multiplication algorithm"""
    # Ensure the input matrices are square
    max_size = max(len(A), len(A[0]), len(B), len(B[0]))
    A = pad_matrix(A, max_size)
    B = pad_matrix(B, max_size)

    # Base case: if the matrices are 1x1, return the product
    if len(A) == 1 and len(A[0]) == 1:
        return [[A[0][0] * B[0][0]]]

    # Split the input matrices into four submatrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Compute the seven products
    p1 = strassen(A11, matrix_subtraction(B12, B22))
    p2 = strassen(matrix_addition(A11, A12), B22)
    p3 = strassen(matrix_addition(A21, A22), B11)
    p4 = strassen(A22, matrix_subtraction(B21, B11))
    p5 = strassen(matrix_addition(A11, A22), matrix_addition(B11, B22))
    p6 = strassen(matrix_subtraction(A12, A22), matrix_addition(B21, B22))
    p7 = strassen(matrix_subtraction(A11, A21), matrix_addition(B11, B12))

    # Compute the four submatrices of the result matrix
    C11 = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    C12 = matrix_addition(p1, p2)
    C21 = matrix_addition(p3, p4)
    C22 = matrix_subtraction(matrix_subtraction(matrix_addition(p5, p1), p3), p7)

    # Combine the four submatrices into the result matrix
    result = [C11, C12, C21, C22]

    # Remove the padding and return the result
    return [[row[i-1] for i in range(len(A))] for row in result]

if __name__ == "__main__":
    # Test the Strassen's algorithm
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    result = strassen(A, B)
    print("Result:")
    for row in result:
        print(row)