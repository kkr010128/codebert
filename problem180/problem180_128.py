N, K = list(map(int, input().split()))
ans = min(N % K, K - (N % K))
print(ans)