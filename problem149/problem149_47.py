n,m,X=map(int,input().split())
c=[list(map(int,input().split())) for i in range(n)]
ans=float('inf')
from itertools import combinations as com
for l in range(1,n+1):
    for i in com(list(range(n)),r=l):
        cnt=[0]*m
        p=0
        for j in i:
            p+=c[j][0]
            for x in range(m):
                cnt[x]+=c[j][x+1]
        if min(cnt)>=X:ans=min(ans,p)
print(ans if ans!=float('inf')else -1)