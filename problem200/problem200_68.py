A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
xyc=[list(map(int,input().split()))for i in range(M)]
ans=min(a)+min(b)
for i in range(M):
    tmp = a[xyc[i][0]-1]+b[xyc[i][1]-1]-xyc[i][2]
    if ans > tmp:
        ans=tmp
print(ans)