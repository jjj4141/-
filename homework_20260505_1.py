import random

n = int(input())

def make_matrix(N):
    matrix = []
    limit = N * N * 10
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.randint(1,limit-1))
        matrix.append(row)

    return matrix

def print_matrix(Matrix):
    for i in range(n):
        for j in range(n):
            print(f"{Matrix[i][j]:4d}", end = "")
        print()

matrices = []

for i in range(3):
    new_matrix = make_matrix(n)
    matrices.append(new_matrix)

matrix_A = matrices[0]
matrix_B = matrices[1]
matrix_C = matrices[2]

result_matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        for u in range(n):
            result_matrix[i][j] += matrix_A[i][u] * matrix_B[u][j]

for i in range(n):
    for j in range(n):
        result_matrix[i][j] += matrix_C[i][j]

print_matrix(result_matrix)
