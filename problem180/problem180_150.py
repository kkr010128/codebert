N, K = map(int, input().split())
ans = min(abs(N-K), N)
if N > K:
    mod = min(N % K, abs(N % K-K))
    ans = min(ans, mod)
print(ans)
