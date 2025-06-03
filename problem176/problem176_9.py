a= list(map(int,input().split()))
N = a[0]
K = a[1]

a = [0]*K
mod = 10**9+7

for x in range(K,0,-1):
    a[x-1] = pow(K//x, N,mod)
    for t in range(2,K//x+1):
        a[x-1] -= a[t*x-1]

s = 0
for i in range(K):
    s += (i+1)*a[i]

ans = s%mod

print(ans)