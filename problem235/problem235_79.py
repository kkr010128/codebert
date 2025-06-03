import math
n = int(input())
a = list(map(int,input().split()))
g = 1
mod = 10**9 + 7
ans = 0
for i in range(n):
    u = (g*a[i])//math.gcd(g,a[i])
    ans *= u//g
    ans %= mod
    ans += u//a[i]
    ans %= mod
    g = u
print(ans)