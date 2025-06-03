X, Y = map(int, input().split())
P = 10 ** 9 + 7
N = (X+Y) // 3
R = (2 * X - Y) // 3
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N+1):
    fact.append((fact[-1] * i) % P)
    inv.append((-inv[P % i] * (P//i) % P))
    factinv.append((factinv[-1] * inv[-1] % P))


def cmb_mod(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p


if (X+Y) % 3 != 0:
    print(0)
else:
    print(cmb_mod(N, R, P))
