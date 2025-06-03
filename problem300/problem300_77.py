def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b
    return a

def factorize(n):
    factor = []
    if n % 2 == 0:
        f = [2, 1]
        n //= 2
        while n % 2 == 0:
            n //= 2
            f[1] += 1
        factor.append(f)

    k = 3
    while k * k <= n:
        if n % k == 0:
            f = [k, 1]
            n //= k
            while n % k == 0:
                n //= k
                f[1] += 1
            factor.append(f)
        k += 2
    if n != 1:
        factor.append([n, 1])
    return factor

a, b = map(int, input().split())
c = gcd(a, b)
f = factorize(c)
print(len(f) + 1)
