def add_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Initialize a result matrix with the same dimensions
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Add corresponding elements of both matrices
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result_matrix

# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrices(matrix1, matrix2)

print("Resultant Matrix:")
for row in result:
    print(row)
