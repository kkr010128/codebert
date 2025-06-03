from math import gcd

A, B = map(int, input().split())

d = gcd(A, B)
ans = 1
i = 2
while i <= pow(d, 1/2)+1:
  if d%i == 0:
    ans += 1
    while d%i == 0:
      d //= i
  i += 1
ans += (d > 1)
print(ans)