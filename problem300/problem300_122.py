from math import ceil
from fractions import gcd

a, b = map(int, input().split())
c = gcd(a, b)
count = 1
for num in range(2, ceil(c**0.5) + 1):
  if c % num == 0:
    count += 1
    while c % num == 0:
      c = c // num
if c > 1:
  count += 1
print(count)