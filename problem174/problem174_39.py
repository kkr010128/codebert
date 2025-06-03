from math import gcd
K = int(input())
sum = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        p = gcd(a, b)
        for c in range(1, K+1):
            sum += gcd(p, c)
print(sum)