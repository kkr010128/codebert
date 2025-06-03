import numpy as np
h,w,m=map(int, input().split())
hw=[tuple(map(int,input().split())) for i in range(m)]
H=np.zeros(h)
W=np.zeros(w)
for i in range(m):
    hi,wi=hw[i]
    H[hi-1]+=1
    W[wi-1]+=1
mh=max(H)
mw=max(W)
hmax=[i for i, x in enumerate(H) if x == mh]
wmax=[i for i, x in enumerate(W) if x == mw]
f=0
for i in range(m):
    hi,wi=hw[i]
    if H[hi-1]==mh and W[wi-1]==mw:
        f+=1
if len(hmax)*len(wmax)-f<1:
    print(int(mh+mw-1))
else:
    print(int(mh+mw))