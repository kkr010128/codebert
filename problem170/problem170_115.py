N, K = map(int,input().split())
ans = 0
MOD = 10**9 + 7
for i in range(K,N+2):
    x = (N+1-i) * i + 1
    ans += x
    ans %= MOD
print (ans)