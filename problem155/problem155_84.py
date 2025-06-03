n,m=map(int,input().split())
H=list(map(int,input().split()))
A=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    A[a].append(b)
    A[b].append(a)
ans=0
for i in range(n):
    for j in A[i]:
        if H[j]>=H[i]:break
    else:
        ans+=1
print(ans)