
# -*- coding: utf-8 -*-

N=int(input())
As=list(map(int, input().split()))

inds=sorted(range(len(As)), key=lambda k: As[k])[::-1]
#ds=[[0 for j in range(N+1-i)] for i in range(N+1)]

ds=[0]
for xy in range(1,N+1):
    i=inds[xy-1] #←
    a=As[i] #←この２行でメモリアクセス省略しないとTLEになる
    nds=[0]*(xy+1)
    nds[-1]=ds[-1]+a*(i-(xy-1))
    nds[0]=ds[0]+a*(N-xy-i)

    for x in range(1,xy):
        y=xy-x
        c1=ds[x-1]+a*abs(i-(x-1))
        c2=ds[x]+a*abs(N-y-i)
        nds[x]=max(c1,c2)
    ds=nds.copy()
    #print(ds)


print(max(ds))
#print(ds)
#print(inds)


