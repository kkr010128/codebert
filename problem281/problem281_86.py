X, Y = map(int, input().split())
MOD = 10 ** 9 + 7


S = -X + 2 * Y
T = 2 * X - Y

if S < 0 or T < 0:
    print(0)
    exit()
if S % 3 != 0 or T % 3 != 0:
    print(0)
    exit()

S //= 3
T //= 3


def cmb(n, r, p):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = 1
    for i in range(n, n - r, -1):
        over = over * i % p
    under = 1
    for i in range(1, r + 1):
        under = under * i % p
    inv = pow(under, p - 2, p)
    return over * inv % p


# print(S, T)
ans = cmb(S + T, S, MOD) % MOD
print(ans % MOD)
