#from random import randint
import numpy as np


def f(h,w,m,ins):
    yp = np.zeros(h,dtype=np.int32)
    xp = np.zeros(w,dtype=np.int32)
    s = set()
    for hi,wi in ins:
        s.add((hi-1,wi-1))
        yp[hi-1] += 1
        xp[wi-1] += 1
    ypm = yp.max()
    xpm = xp.max()
    yps = np.where(yp == ypm)[0].tolist()
    xps = np.where(xp == xpm)[0].tolist()
    ans = yp[yps[0]]+xp[xps[0]]
    for ypsi in yps:
        for xpsi in xps:
            if not (ypsi,xpsi) in s:
                return ans
    return ans-1

if __name__ == "__main__":
    if False:
        while True:
            h,w = randint(1,10**5*3),randint(10**5,10**5*3)
            m = randint(1,min(h*w,10**5*3))
            ins = [(randint(1,h),randint(1,w)) for i in range(m)]
            ans = f(h,w,m,ins)
            print(ans)
    else:
        h,w,m = map(int,input().split())
        ans = f(h,w,m,[list(map(int,input().split())) for i in range(m)])
        print(ans)
