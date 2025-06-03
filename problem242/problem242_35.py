import sys
import time
input = sys.stdin.readline

mod = 10 ** 9 + 7


def inv(x):
    return modpow(x, mod - 2)


def modpow(a, x):
    if x == 0:
        return 1
    elif x % 2 == 0:
        return modpow((a * a) % mod, x // 2)
    else:
        return (modpow((a * a) % mod, x // 2) * a) % mod


N, K = map(int, input().strip().split(" "))
A = list(map(int, input().strip().split(" ")))
A.sort()

if K == 1:
    print(0)
else:
    fact = [1, 1]
    inv_fact = [1, 1]

    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % mod)
        inv_fact.append(inv(fact[-1]))
    nck = [0 if i < K - 1 else (((fact[i] * inv_fact[K - 1]) % mod) * inv_fact[i - K + 1]) % mod for i in range(0, N + 1)]
    min_sum, max_sum = 0, 0
    for i in range(1, N + 1):
        if 1 <= i <= N - K + 1:
            min_sum += (nck[N - i] * A[i - 1]) % mod
        if K <= i <= N:
            max_sum += (nck[i - 1] * A[i - 1]) % mod

    ans = max_sum - min_sum
    while ans < 0:
        ans += mod
    print(ans % mod)