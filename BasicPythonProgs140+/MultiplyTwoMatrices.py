"""
Program 38: Write a Python Program to Multiply Two Matrices.
"""


# function to multiply 2 matrices
def multiply_matrices(mat1, mat2):
    # Determine the dimensions of the 2 matrices
    rows1 = len(mat1)
    rows2 = len(mat2)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])

    # check if the multiplication is possible
    if cols1 != rows2:
        return "Matrix multiplication is not possible."

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


# The given matrices
mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]
mat2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Calling the function to multiply the matrices
result_matrix = multiply_matrices(mat1, mat2)

# Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrix multiplication: ")
    for row in result_matrix:
        print(row)

"""
Output:
Result of matrix multiplication: 
[58, 64]
[139, 154]
"""
