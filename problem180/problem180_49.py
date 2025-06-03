N,K=map(int,input().split())

if N > K:
    N %= K
ans = min(N, K-N)

print(ans)