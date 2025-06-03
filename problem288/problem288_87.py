n = int(input())
from math import sqrt, ceil
for i in range(1, ceil(sqrt(n)) + 1):
    if n % i == 0:
        ans = i

print(ans-1 + (n//ans)-1)