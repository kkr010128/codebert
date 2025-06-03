from bisect import *
from math import *
N,D,A=map(int,input().split())
monsters=[list(map(int,input().split())) for _ in range(N)]
monsters.sort(key=lambda x:x[0])
killingrange=[0]*N
monsterspoint=[]
monstershp=[]
imos=[0]*N
for i in range(N):
    monsterspoint.append(monsters[i][0])
    monstershp.append(monsters[i][1])
for i in range(N):
    ind=bisect(monsterspoint,monsterspoint[i]+2*D)
    killingrange[i]=ind
#print(killingrange)
cnt=0
for i in range(N):
    monstershp[i]=monstershp[i]+imos[i]
    if (monstershp[i]>0):
        cnt=cnt+ceil(monstershp[i]/A)
        imos[i]=imos[i]-A*ceil(monstershp[i]/A)
        if killingrange[i]<N:
            imos[killingrange[i]]=imos[killingrange[i]]+A*ceil(monstershp[i]/A)
        monstershp[i]=monstershp[i]-A*ceil(monstershp[i]/A)
    if i<N-1:
        imos[i+1]=imos[i]+imos[i+1]
    #print(monstershp,imos)
print(cnt)