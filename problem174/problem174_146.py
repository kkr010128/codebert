import math

k = int(input())
s = 0

def gcd3(a, b, c):
    d = math.gcd(a, b)
    e = math.gcd(d, c)
    return e


for a in range(1, k+1):
    for b in range(a, k+1):
        for c in range(b, k+1):
            d = gcd3(a, b, c)
            if a == b and b == c:
                s += d
            elif a == b or b == c:
                s += d * 3
            else:
                s += d * 6

print(s)
