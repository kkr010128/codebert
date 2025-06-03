n,m,k = map(int,input().split())
ans = 0
mod = 998244353
p = [0 for i in range(n)]
p[0] = 1
for i in range(n-1):
    p[i+1] = p[i]*(i+2)%mod
p.append(1)
for i in range(k+1):
    u = pow(m-1,n-1-i,mod)
    s = p[n-2]*pow(p[i-1],mod-2,mod)*pow(p[n-i-2],mod-2,mod)
    ans = (ans + m*u*s)%mod
print(ans)