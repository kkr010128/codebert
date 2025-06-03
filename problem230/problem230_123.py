import bisect
import math
N,D,A=map(int,input().split())
tmp=[list(map(int,input().split())) for i in range(N)]
tmp.sort(key=lambda x:x[0])
monster=[];X=[]
for i in range(N):
    monster.append(tmp[i][1]);X.append(tmp[i][0])
minus=[0]*(N+1)
ans=0
damage=0
for i in range(N):
    damage-=minus[i]
    monster[i]=max(0,monster[i]-damage)
    if(monster[i]==0):
        continue
    cnt=math.ceil(monster[i]/A)
    monster[i]=0
    ans+=cnt
    b=bisect.bisect_left(X,X[i]+2*D+1)
    minus[b]+=cnt*A
    damage+=A*cnt
print(ans)