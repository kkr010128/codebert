N, *X = map(int, open(0).read().split())
ans = float("inf")
for x in range(min(X), max(X) + 1):
    cur = 0
    for j in range(N):
        cur += (X[j] - x) ** 2
    ans = min(ans, cur)
print(ans)
