import os
import sys
import numpy as np

def solve(N, K, S, P, R, T):
    dp = np.zeros((N+1, 3), dtype=np.int64)
    for i in range(1, N+1):
        c = T[i]
        dp[i, 0] = max(dp[i-K, 1], dp[i-K, 2]) + (c == "r") * R
        dp[i, 1] = max(dp[i-K, 0], dp[i-K, 2]) + (c == "s") * S
        dp[i, 2] = max(dp[i-K, 0], dp[i-K, 1]) + (c == "p") * P
    #d = dp.max(1)
    d = np.zeros(N+1, dtype=np.int64)
    for i in range(N+1):
        d[i] = dp[i].max()
    ans = d[-K:].sum()
    return ans


# >>> numba compile >>>
numba_config = [
    [solve, "i8(i8,i8,i8,i8,i8,string)"],
]
if sys.argv[-1] == "ONLINE_JUDGE":
    from numba import njit
    from numba.pycc import CC
    cc = CC("my_module")
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature)(func)
        cc.export(func.__name__, signature)(func)
    cc.compile()
    exit()
elif os.name == "posix":
    exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
else:
    from numba import njit
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature, cache=True)(func)
    print("compiled!", file=sys.stderr)
# <<< numba compile <<<


def main():
    N, K = map(int, input().split())
    S, P, R = map(int, input().split())
    T = "_" + input()
    ans = solve(N, K, S, P, R, T)
    print(ans)

main()
