import math

def f_gcd(a, b):
    return math.gcd(a, b)

k = int(input())

ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += f_gcd(math.gcd(a, b), c)

print(ans)