def nCr(n,r,fac,finv):
    mod = (10**9)+7
    ans = fac[n] * (finv[r] * finv[n-r] % mod) % mod
    return ans
k = int(input())
s = input()
l = len(s)
n = l+k+1
# als = list(map(int,input().split()))
# als.sort()
ans = 0
mod = (10**9)+7
fac = [1,1]+[0]*n
finv = [1,1]+[0]*n
inv = [1,1]+[0]*n
for i in range(2,n+1):
    fac[i] = fac[i-1] * i % mod
    inv[i] = mod - inv[mod%i] * (mod//i) % mod
    finv[i] = finv[i-1] * inv[i] % mod
for i in range(k+1):
    ans += nCr(l-i+k-1,l-1,fac,finv)*pow(26,i,mod)*pow(25,k-i,mod)
    ans %= mod
print(ans)