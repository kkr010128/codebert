from math import gcd

magic = [2, 7, 61]

def mul(a, b, n):
    # calculate (a * b) % n
    r, a, b = 0, a % n, b % n
    while b:
        if b & 1:
            r = (a + r) % n
        a = (a + a) % n
        b >>= 1
    return r

def bigmod(a, p, n):
    # calculate (a ** p) % n
    if p == 0:
        return 1
    if p == 1:
        return a % n
    return mul(bigmod(mul(a, a, n), p // 2, n), a if p % 2 else 1, n)

def miller_rabin(n, a):
    if gcd(a, n) == n:
        return True
    if gcd(a, n) != 1:
        return False
    d, r = n-1, 0
    while d % 2 == 0:
        d /= 2
        r += 1
    res = bigmod(a, d, n)
    if res == 1 or res == n-1:
        return True
    while r:
        r -= 1
        res = mul(res, res, n)
        if res == n-1:
            return True
    return False

def isPrime(n):
    for a in magic:
        if not miller_rabin(n, a):
            return False
    return True


num = int(input())
ans = sum(map(int, [isPrime(int(input())) for _ in range(num)]))
print(ans)

