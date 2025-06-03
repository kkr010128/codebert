import numpy as np
import sys
x, y = map(int, input().split())

if (x + y) % 3 != 0 or x > 2 * y or y > 2 * x:
    print(0)
    sys.exit()

# 手数
n = (x + y) // 3
x -= n
y -= n

MOD = 10**9 + 7

# モジュラ逆数戦法
def prepare(n, MOD):

    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD
    fn = f

    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return fn, invs


fact, invs = prepare(n, MOD)

print(fact * invs[x] * invs[y] % MOD)