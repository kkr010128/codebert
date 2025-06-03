from numba import njit
import numpy as np

d = int(input())
cs = list(map(int, input().split()))
cs = np.array(cs, dtype=np.int64)
sm = [list(map(int, input().split())) for _ in range(d)]
sm = np.array(sm, dtype=np.int64)

@njit('i8(i8[:], i8)', cache=True)
def total_satisfaction(ts, d):
    ls = np.zeros(26, dtype=np.int64)
    s = 0
    for i in range(d):
        t = ts[i]
        t -= 1
        s += sm[i][t]
        ls[t] = i + 1

        dv = cs * ((i+1) - ls)
        s -= dv.sum()
    return s

@njit('i8(i8, i8, i8, i8, i8[:])', cache=True)
def differential(s, i, t, d, ls):
    t -= 1
    bk = ls[t]
    s += sm[i][t]
    ls[t] = i + 1

    dv = cs * ((i+1) - ls)
    s -= dv.sum()

    ls[t] = bk
    return s

ts = np.array([], dtype=np.int64)
for i in range(d):
    sc = 0
    if len(ts) > 0:
        tt = np.array(ts, dtype=np.int64)
        sc = total_satisfaction(tt, i)

    ls = np.zeros(26, np.int64)
    for i, t in enumerate(ts, 1):
        ls[t-1] = i

    mx = -99999999
    mxt = -1
    for t in range(1, 26+1):
        df = differential(sc, len(ts), t, i + 1, ls)
        s = sc + df
        if s > mx:
            mx = s
            mxt = t
    ts = np.append(ts, [mxt])
    print(mxt)
