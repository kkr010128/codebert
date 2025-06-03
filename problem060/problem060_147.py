n, m, l = map(int, input().split())

A = []
for g in range(n):
    A.append(list(map(int, input().split())))

B = []
for h in range(m):
    B.append(list(map(int, input().split())))

for i in range(n):
    output = []
    for j in range(l):
        temp = 0
        for k in range(m):
            temp += A[i][k] * B[k][j]
        output.append(temp)
    print(*output)