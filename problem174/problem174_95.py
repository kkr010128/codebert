import math


K = int(input())
result = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        r = math.gcd(a, b)
        for c in range(1, K+1):
            result += math.gcd(r, c)

print(result)
