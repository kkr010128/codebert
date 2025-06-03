from math import gcd

K = int(input())

ans = 0

for h in range(1, K+1):
  for i in range(1, K+1):
    for j in range(1, K+1):
      ans += gcd(h, gcd(i, j))

print(ans)