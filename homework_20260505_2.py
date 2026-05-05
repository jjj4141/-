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

matrix_A = make_matrix(n)

result_matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        result_matrix[i][j] = matrix_A[j][i]

print_matrix(result_matrix)
