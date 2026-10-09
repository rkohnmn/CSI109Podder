# Check if a matrix is symmetric
matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

# Compare matrix[i][j] with matrix[j][i]
is_symmetric = True
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False

print("Matrix:", matrix)
print("Is symmetric:", is_symmetric)
