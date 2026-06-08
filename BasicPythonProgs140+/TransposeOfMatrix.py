"""
Program 39: Write a Python Program to Transpose a Matrix.
"""

# defining a function to transpose a matrix
def transpose_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Create an empty matrix to store the transposed data
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = mat[i][j]
    return transposed_matrix

# Input matrix
mat = [
    [1,2,3],
    [4,5,6]
]

# Transpose the matrix
transposed_matrix = transpose_matrix(mat)

# Print the transposed matrix
print("Transposed matrix: ")
for row in transposed_matrix:
    print(row)

"""
Output:
Transposed matrix: 
[1, 4]
[2, 5]
[3, 6]
"""