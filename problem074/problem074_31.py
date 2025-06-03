import numpy as np
from numba import njit
from numba.types import i8
ni8 = np.int64
MOD = 998244353


@njit((i8[:,::-1], i8[:], i8, i8), cache=True)
def solve(lr, dp, n, k):
    acc_dp = np.ones_like(dp)
    for i in range(1, n):
        val = 0
        for j in range(k):
            a = i - lr[j, 0]
            if a < 0:
                continue
            b = i - lr[j, 1] - 1
            val += acc_dp[a] - (acc_dp[b] if b >= 0 else 0)
        dp[i] = val % MOD
        acc_dp[i] = (acc_dp[i - 1] + dp[i]) % MOD
    return dp[n - 1]


def main():
    f = open(0)
    n, k = [int(x) for x in f.readline().split()]
    lr = np.fromstring(f.read(), ni8, sep=' ').reshape((-1, 2))
    dp = np.zeros(n, ni8)
    dp[0] = 1
    ans = solve(lr, dp, n, k)
    print(ans)

main()