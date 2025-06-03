import os
import sys

import numpy as np


def solve(inp):
    r, c, k = inp[:3]
    items = np.zeros((r + 1, c + 1), dtype=np.int64)
    rrr = inp[3::3]
    ccc = inp[4::3]
    vvv = inp[5::3]
    for r_, c_, v in zip(rrr, ccc, vvv):
        items[r_, c_] = v

    dp = np.zeros((r + 1, c + 1, 4), dtype=np.int64)

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            v = items[i, j]
            dp[i, j] = np.maximum(dp[i, j - 1], dp[i - 1, j, 3])
            if v > 0:
                dp[i, j, 1:] = np.maximum(dp[i, j, 1:], dp[i, j, :-1] + v)

    return dp[-1, -1, -1]


if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    # noinspection PyUnresolvedReferences
    from my_module import solve
else:
    from numba import njit

    solve = njit('(i8[:],)', cache=True)(solve)
    print('compiled', file=sys.stderr)

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print(ans)
