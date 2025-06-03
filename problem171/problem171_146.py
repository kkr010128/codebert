def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        exit()
    elif os.name == "posix":
        exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
        for func, _ in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print("compiled!", file=sys.stderr)

import numpy as np

def solve(N, A):
    # dp[n][k] := n 人目まで見て左に k 人送ったときの最大値
    A_order = np.argsort(-A)
    dp = np.zeros((N+2, N+2), dtype=np.int64)
    for n in range(1, N+1):
        idx_A = A_order[n-1]
        a = A[idx_A]
        for k in range(n+1):
            dp[n, k] = max(
                dp[n-1, k-1] + a * abs(idx_A-(k-1)) if k>0 else 0,  # 左に送る
                dp[n-1, k] + a * abs(idx_A-(N-n+k)) if k<n else 0,  # 右に送る
            )
    return dp[N].max()

numba_compile([
    [solve, "i8(i8,i8[:])"],
])

N = int(input())
A = np.array(input().split(), dtype=np.int64)
ans = solve(N, A)
print(ans)
