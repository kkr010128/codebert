N, M, X = map(int, input().split())
BOOKS = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10 ** 8
ans = INF
for selection in range(1 << N):
    price = 0
    values = [0] * M
    for i in range(N):
        if selection & (1 << i):
            x = BOOKS[i]
            price += x[0]
            for j in range(M):
                values[j] += x[j+1]
    if all(v >= X for v in values):
        ans = min(ans, price)

if ans == INF:
    print(-1)
else:
    print(ans)