n, m, l = map(int, input().split())
matrix_a = [list(map(int, input().split())) for i in range(n)]
matrix_b = [list(map(int, input().split())) for i in range(m)]
mul_matrix_a_b = [[sum([matrix_a[i][k] * matrix_b[k][j] for k in range(m)]) for j in range(l)] for i in range(n)]
for result in mul_matrix_a_b:
    print(*result)