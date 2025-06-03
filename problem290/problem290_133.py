import numpy as np
from numba import njit

@njit
def solve(stdin):
    n, k = stdin[:2]
    A = stdin[2: 2 + n]
    A = np.sort(A)[::-1]
    F = np.sort(stdin[2 + n:])

    def is_ok(x):
        tmp = 0
        for a, f in zip(A, F):
            y = a * f
            if y > x:
                tmp += a - x // f
        return tmp <= k

    ok = 10 ** 16
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return ok

print(solve(np.fromstring(open(0).read(), dtype=np.int64, sep=' ')))