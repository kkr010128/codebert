from collections import defaultdict
h,w,m = map(int,input().split())
dh = defaultdict(int)
dw = defaultdict(int)
l=defaultdict(tuple)
for _ in range(m):
    x,y = map(int,input().split())
    dh[x]+=1
    dw[y]+=1
    l[(x,y)]=1
m = 0
for i in range(1,h+1):
    if dh[i]>m:
        m = dh[i]
        hi=i
c=m
m = 0
for i in range(1,w+1):
    d = dw[i]
    if l[(hi,i)]==1:
        d-=1
    m = max(m,d)
c+=m
m = 0
wi=0
for i in range(1,w+1):
    if dw[i]>m:
        m = dw[i]
        wi=i
c2=m
m = 0
for i in range(1,h+1):
    d = dh[i]
    if l[(i,wi)]==1:
        d-=1
    m = max(m,d)
c2+=m
print(max(c,c2))