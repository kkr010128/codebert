import math
def prime(g):
    l = []
    p = 2
    while p * p <= g:
        if g % p != 0:
            p += 1
            continue
        while g % p == 0:
            g //= p
        l.append(p)
        p += 1
    if g != 1:
        l.append(g)
    return len(l)

a, b = map(int, input().split())
g = math.gcd(a, b)
print(prime(g) + 1)
