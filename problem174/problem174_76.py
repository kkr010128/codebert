from math import gcd

K = int(input())

ans = 0
r = range(1, K+1)
for i in r:
    for j in r:
        for k in r:
            ans += gcd(gcd(i, j), k)

print(ans)
