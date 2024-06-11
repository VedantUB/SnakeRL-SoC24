
def matrix_multiply(A, B):
    C = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_power(A, num):
    if num == 1:
        return A
    else:
        return matrix_multiply(A, matrix_power(A, num - 1))

matrix_A = [
    [1, 0, 0, 0],
    [0.5, 0, 0.5, 0],
    [0, 0.2, 0, 0.8],
    [0, 0, 0, 1]
]

# Here value of T can be changed
T = 3

final_matrix = matrix_power(matrix_A, T)

# This will print the probabilities of reaching state Sa, Sb, Sc and Sd from Sa
print(final_matrix[0])


