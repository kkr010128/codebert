n,m,l = [int(x) for x in input().split()]
matrix_a = [[int(x) for x in input().split()] for _ in range(n)]
matrix_b = [[int(x) for x in input().split()] for _ in range(m)]
matrix_ab = [[0 for a in range(l)] for b in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            matrix_ab[i][j] += matrix_a[i][k]*matrix_b[k][j]
for i in range(n):
    for j in range(l):
        if j < l-1:
            print(matrix_ab[i][j], "", end="")
        elif j == l-1:
            print(matrix_ab[i][j])