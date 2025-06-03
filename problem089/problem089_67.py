h,w,m=map(int,input().split())
HH=[]
WW=[]
HW=set()
lh=[0]*(h+1)
lw=[0]*(w+1)
for _ in range(m):
    h1,w1=map(int,input().split())
    lh[h1]+=1
    lw[w1]+=1
    HW.add((h1,w1))
lhmax=max(lh)
lwmax=max(lw)
maxh=[]
maxw=[]
for i in range(1,h+1):
    if lh[i]==lhmax:
        maxh.append(i)
for i in range(1,w+1):
    if lw[i]==lwmax:
        maxw.append(i)

if len(maxh)*len(maxw)>m:
    print(lhmax+lwmax)
else:
    flag=True
    for i in maxh:
        for j in maxw:
            if (i,j) not in HW:
                flag=False
                break
    if flag==True:
        print(lhmax+lwmax-1)
    else:
        print(lhmax+lwmax)