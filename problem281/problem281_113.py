def comb(n, r):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod

X, Y = map(int, input().split())
mod = 10 ** 9 + 7
if (X + Y) % 3:
    print(0)
else:
    if 2 * Y - X < 0 or 2 * X - Y < 0:
        print(0)
    else:
        n = (X + Y) // 3
        r = (2 * Y - X) // 3
        print(comb(n, r))
