# 貪欲法 + 山登り法 + スワップ操作
import time
s__ = time.time()
limit = 1.9
#limit = 10

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

@njit('i8[:]()', cache=True)
def greedy():
    ts = np.array([0] * d, dtype=np.int64)
    for i in range(d):
        mx = -1e10
        mxt = None
        for t in range(1, 26+1):
            ts[i] = t
            s = total_satisfaction(ts, i + 1)
            if s > mx:
                mx = s
                mxt = t
        ts[i] = mxt
    return ts

@njit('i8(i8, i8[:])', cache=True)
def loop(mxsc, ts):
    it = 50
    rds = np.random.randint(0, 4, (it,))
    rdd = np.random.randint(1, d, (it,))
    rdq = np.random.randint(1, 26, (it,))
    rdx = np.random.randint(1, 12, (it,))
    for i in range(it):
        bk1 = 0
        bk2 = 0
        if rds[0] == 0:
            # trailing
            di = rdd[i]
            qi = rdq[i]

            bk1 = ts[di]
            ts[di] = qi
        else:
            # swap
            di = rdd[i]
            xi = rdx[i]
            if di + xi >= d:
                xi = di - xi
            else:
                xi = di + xi
            
            bk1 = ts[di]
            bk2 = ts[xi]
            ts[di] = bk2
            ts[xi] = bk1

        sc = total_satisfaction(ts, d)

        if sc > mxsc:
            #print(mxsc, '->', sc)
            mxsc = sc
        else:
            # 最大値を更新しなかったら戻す
            if rds[0] == 0:
                ts[di] = bk1
            else:
                ts[di] = bk1
                ts[xi] = bk2

    return mxsc

ts = greedy()
mxsc = total_satisfaction(ts, d)
mxbk = mxsc

s_ = time.time()
mxsc = loop(mxsc, ts)
e_ = time.time()

consume = s_ - s__
elapsed = e_ - s_
#print('consume:', consume)
#print('elapsed:', elapsed)

if consume < limit:
    lp = int((limit - consume)/ elapsed)
    #print('loop', lp)
    for _ in range(lp):
        mxsc = loop(mxsc, ts)

for t in ts:    print(t)
#print(mxbk, mxsc)
#print(time.time() - s__)
