N = int(input())

c = [[0 for _ in range(10)] for __ in range(10)]
for x in range(1, N+1):
    check = str(x)
    it = int(check[0])
    jt = int(check[-1])
    c[it][jt] += 1

ans = 0
for i in range(0,10):
    for j in range(0,10):
        ans += c[i][j] * c[j][i]

print(ans)
