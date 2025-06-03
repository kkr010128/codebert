n, m, l =map(int, input().split())
A = []
B = []
C = []
for i in range(n):
    i = list(map(int, input().split()))
    A.append(i)

for i in range(m):
    i = list(map(int, input().split()))
    B.append(i)
#積を求める

for i in range(n):
    line = []
    for j in range(l):
        c = 0
        for k in range(m):
            c += A[i][k] * B[k][j]
        line.append(c)
    C.append(line)
#形式に合わせて出力する
for line in C:
    print(*line)
