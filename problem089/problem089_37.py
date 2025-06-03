H,W,M=map(int,input().split())
h,w=map(list,zip(*[list(map(int,input().split())) for i in range(M)]))
from collections import Counter
hc,wc=Counter(h),Counter(w)
hx,wx=hc.most_common()[0][1],wc.most_common()[0][1]
hl,wl=set([k for k,v in hc.items() if v==hx]),set([k for k,v in wc.items() if v==wx])
x=sum([1 for i in range(M) if h[i] in hl and w[i] in wl])
print(hx+wx if len(hl)*len(wl)-x else hx+wx-1)