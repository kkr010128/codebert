a,b,m=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
xyc=[list(map(int,input().split())) for _ in range(m)]

ans=min(al)+min(bl)
for i in range(m):
    tmp=0
    tmp=al[xyc[i][0]-1]+bl[xyc[i][1]-1]-xyc[i][2]
    ans=min(ans,tmp)
print(ans)