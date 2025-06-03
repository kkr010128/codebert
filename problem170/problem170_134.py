N, K = map(int,input().split())
MOD = 10**9 + 7
ans = 0
for k in range(K,N+2):
    m = (k*(k-1))//2
    M = (k*(N+N-k+1))//2
    ans += M-m+1

print(ans%MOD)
