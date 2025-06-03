N, K = [int(_) for _ in input().split()]
P = [int(_) for _ in input().split()]

ans = 0.0
k = 0
v = 0.0
for i in range(N):
    v += (P[i] + 1) / 2
    k += 1
    if k > K:
        v -= (P[i-K] + 1) / 2
        k -= 1
    ans = max(ans, v)
print(ans)
