MAX = 4*10**5
bikkuri=[1]
mod = 10**9+7
for i in range(1,MAX+1):
    bikkuri.append((bikkuri[-1]*i)%mod)

def Comb(n,k):
    ans = bikkuri[n]*pow(bikkuri[k],mod-2,mod)*pow(bikkuri[n-k],mod-2,mod)
    ans %=mod
    return ans
    
n,k = map(int,input().split())
if n-1 <= k:
    ans = Comb(2*n-1,n)
    print(ans)
else:
    tmp = 0
    for i in range(k+1):
        tmp += Comb(n,i)*Comb(n-1,i)
        tmp %= mod
    print(tmp)