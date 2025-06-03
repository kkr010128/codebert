from math import gcd
K = int(input())
ans = 0
for i in range(1, K+1):
    for j in range(i+1, K+1):
        for k in range(j+1, K+1):
            ans += gcd(gcd(i, j), k)*6

for i in range(1, K+1):
    for j in range(i+1, K+1):
        ans += gcd(i, j)*6

ans += K*(K+1)//2

print(ans)
