import os
import sys
import numpy as np

def solve(N, M, A):
    # n 以上上がる方法だけを試した時に、M 回以上の握手を行うことができるか
    ok = 0
    ng = 202020
    while ok + 1 < ng:
        c = ok+ng >> 1
        cnt = 0
        idx_A = N-1
        for a1 in A:
            while idx_A >= 0 and A[idx_A]+a1 < c:
                idx_A -= 1
            cnt += idx_A + 1
        if cnt >= M:
            ok = c
        else:
            ng = c
    idx_A = N-1
    cum_A = np.zeros(len(A)+1, dtype=np.int64)
    cum_A[1:] = np.cumsum(A)
    ans = 0
    cnt = 0
    for a1 in A:
        while idx_A >= 0 and A[idx_A]+a1 < ok:
            idx_A -= 1
        cnt += idx_A + 1
        ans += cum_A[idx_A+1] + (idx_A+1)*a1
    ans -= (cnt-M) * ok
    return ans


# >>> numba compile >>>
numba_config = [
    [solve, "i8(i8,i8,i8[:])"],
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
    N, M = map(int, input().split())
    A = np.array(sorted(map(int, input().split()), reverse=True), dtype=np.int64)
    ans = solve(N, M, A)
    print(ans)

main()
