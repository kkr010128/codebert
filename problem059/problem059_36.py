r, c = map(int, input().split())
matrix = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    a = list(map(int, input().split()))
    for j in range(c):
        matrix[i][j] = a[j]
    matrix[i][c] = sum(a)
for l in range(c+1):
    for m in range(r):
        matrix[r][l] += matrix[m][l]

for cv in range(r+1):
    for fv in range(c+1):
        print(matrix[cv][fv], end='')
        if fv != c:
            print(" ", end='')
    print()
