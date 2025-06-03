import math
mod = 10**9+7
n,k = map(int,input().split())
b = math.factorial(k-1)%mod
fact = [0]*(n-k+1)
a = math.factorial(k-1)%mod
c = 1
for i in range(k-1, n):
    if i == k-1:
        fact[0] = (a*pow(b*c, mod-2, mod))%mod
    else:
        a = a*i%mod
        c = c*(i-k+1)%mod
        fact[i-k+1] = (a*pow(b*c, mod-2, mod))%mod
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(k-1,n):
    ans += fact[i-k+1]*(A[i]-A[n-i-1])
    ans %= mod
print(ans)
