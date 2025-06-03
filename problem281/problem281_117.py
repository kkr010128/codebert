def binom(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)

    res = factinv[r] % p
    for i in range(r):
        res = res * (n - i) % p

    return fact[n] * factinv[r] * factinv[n-r] % p

X, Y = list(map(int, input().split()))

p = 10 ** 9 + 7

if X % 3 == 2 * Y % 3 and 2 * X % 3 == Y % 3:
    a = (2 * X - Y) // 3
    b = (2 * Y - X) // 3

    if a >= 0 and b >= 0:
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]
        
        for i in range(2, a + b + 1):
            fact.append((fact[-1] * i) % p)
            inv.append((-inv[p % i] * (p // i)) % p)
            factinv.append((factinv[-1] * inv[-1]) % p)

        print(binom(a + b, a))
    else:
        print(0)
else:
    print(0)