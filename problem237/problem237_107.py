N = int(input())

ST = []
for i in range(N):
    X, L = map(int, input().split())
    ST.append((X - L, X + L))

ST.sort(key=lambda x: x[1])

ans = 0
cur = -1e9
for i in range(N):
    S, T = ST[i]
    if cur <= S:
        ans += 1
        cur = T
print(ans)
