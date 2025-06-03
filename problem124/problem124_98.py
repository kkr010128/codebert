k = int(input())
s = input()
mod=10**9+7
n=len(s)

framod=[1]
def framod_calc(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
        framod.append(a)
framod_calc(n+k+1, mod)

def combmod(n, k, mod):
    a=framod[n]
    b=framod[k]
    c=framod[n-k]
    return (a * pow(b, mod-2, mod) * pow(c, mod-2, mod)) % mod

ans=0
for i in range(k+1):
    ans+=(pow(26, i, mod)*pow(25, k-i, mod))*combmod(n+(k-i)-1, n-1, mod)
    ans%=mod
print(ans)