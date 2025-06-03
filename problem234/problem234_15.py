n = int(input())
c = [[0] * 10 for _ in range(10)]

for i in range(1, n + 1):
    a = int(str(i)[0])
    b = int(str(i)[-1])
    c[a][b] += 1

res = 0
for i in range(10):
    for j in range(10):
        res += c[i][j]*c[j][i]
print(res)
