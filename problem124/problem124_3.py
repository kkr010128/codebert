k = int(input())
n = len(input())
mod = pow(10,9)+7
c = 1
ans = pow(26,k,mod)
for i in range(1,k+1):
    c *= (i+n-1)*pow(i,mod-2,mod)
    c %= mod
    ans += (c*pow(25,i,mod)*pow(26,k-i,mod))
    ans %= mod
print(ans)