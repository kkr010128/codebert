import sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    import os
    import re
    with open(__file__) as f:
        source = f.read().split('###''nbacl')
    for s in source[1:]:
        s = re.sub("'''.*", '', s)
        sp = s.split(maxsplit=1)
        if os.path.dirname(sp[0]):
            os.makedirs(os.path.dirname(sp[0]), exist_ok=True)
        with open(sp[0], 'w') as f:
            f.write(sp[1])
    from nbmodule import cc
    cc.compile()
import numpy as np
from numpy import int64
from nbmodule import solve


f = open(0)
N, M = [int(x) for x in f.readline().split()]
AB = np.fromstring(f.read(), dtype=int64, sep=' ').reshape((-1, 2))
ans = solve(N, AB)
print(ans)

'''
###nbacl nbmodule.py
import numpy as np
from numpy import int64
from numba import njit
from numba.types import i8
from numba.pycc import CC
import nbacl.dsu as dsu
cc = CC('nbmodule')


@cc.export('solve', (i8, i8[:, ::1]))
def solve(N, AB):
    t = np.full(N, -1, dtype=int64)
    for i in range(AB.shape[0]):
        dsu.merge(t, AB[i, 0] - 1, AB[i, 1] - 1)
    ret = 0
    for _ in dsu.groups(t):
        ret += 1
    return ret - 1

if __name__ == '__main__':
    cc.compile()

###nbacl nbacl/dsu.py
import numpy as np
from numpy import int64
from numba import njit


@njit
def dsu(t):
    t = -1


@njit
def merge(t, x, y):
    u = leader(t, x)
    v = leader(t, y)

    if u == v:
        return u

    if -t[u] < -t[v]:
        u, v = v, u

    t[u] += t[v]
    t[v] = u

    return u


@njit
def same(t, x, y):
    return leader(t, x) == leader(t, y)


@njit
def leader(t, x):
    if t[x] < 0:
        return x
    t[x] = leader(t, t[x])
    return t[x]


@njit
def size(t, x):
    return -t[leader(t, x)]


@njit
def groups(t):
    for i in range(t.shape[0]):
        if t[i] < 0:
            yield i

'''