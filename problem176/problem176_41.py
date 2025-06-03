k,n = map(int,input().split())

ns = [0] * n
ans = 0

def modpow(a,n,mod=1000000007):
    if n==0:
        return 1
    elif n%2==0:
        return modpow(a*a%mod, n//2, mod)
    else:
        return a * modpow(a,n-1,mod) % mod

for i in range(n,0,-1):
    # ns[i-1] = ((n//i)**k) % (10**9+7)
    ns[i-1] = modpow(n//i,k)
    for j in range(2*i,n+1,i):
        ns[i-1] -= ns[j-1]
    ans += (i * ns[i-1])%(10**9+7)
    ans %= (10**9+7)

print(ans)