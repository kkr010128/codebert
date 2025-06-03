N, K = map(int, input().split())

N = N - (N // K)*K
ans = min(N, K-N)

print(ans)