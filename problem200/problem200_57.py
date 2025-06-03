A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
xyc=[]
for i in range(M):
    tmp=list(map(int,input().split()))
    xyc.append(tmp)
ans=min(a)+min(b)
judge=[a[v[0]-1]+b[v[1]-1]-v[2] for v in xyc]
print(min(ans,min(judge)))