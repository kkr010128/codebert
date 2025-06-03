n, m, l = map(int, raw_input().split())
matrix_a = []
matrix_b = []

for i in range(n):
    line = map(int, raw_input().split())
    matrix_a.append(line)
for i in range(m):
    line = map(int, raw_input().split())
    matrix_b.append(line)


for i in range(n):
    result = []
    for j in range(l):
        tmp = 0
        for k in range(m):
            tmp += matrix_a[i][k] * matrix_b[k][j]
        result.append(tmp)
    print " ".join(map(str, result))