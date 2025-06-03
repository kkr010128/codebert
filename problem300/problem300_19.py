from fractions import gcd

def factorization(n):
    res = []
    m = 2
    while m ** 2 <= n:
        if n % m == 0:
            cnt = 0
            while n % m == 0:
                cnt += 1
                n //= m
            res.append([m, cnt])
        m += 1

    if n > 1:
        res.append([n, 1])

    return res


a, b = map(int, input().split())
print(len(factorization(gcd(a, b))) + 1)