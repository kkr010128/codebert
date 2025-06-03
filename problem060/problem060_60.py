n, m, l  = [int(_) for _ in input().split()]
matrix1 = []
for i in range(n):
    matrix1.append([int(_) for _ in input().split()])
matrix2 = []
for i in range(m):
    matrix2.append([int(_) for _ in input().split()])

for i in range(n):
    for j in range(l):
        x = 0
        for k in range(m):
            x += matrix1[i][k] * matrix2[k][j]
        print(x, end=" " if j < l - 1 else "\n")

