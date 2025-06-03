N,K = map(int,input().split())
MOD = 10**9+7
s = 1
for k in range(K,N+1):
    t = (N+1-k)*k+1
    # print(t)
    s += t
    s = s%MOD
print(s)

