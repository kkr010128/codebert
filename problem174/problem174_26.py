import math
n = int(input())
s = 0
for a in range(n):
    for b in range(n):
        d = math.gcd(a + 1, b + 1)
        for c in range(n):
            s += math.gcd(c + 1, d)
print(s)