N=int(input())
Xlist=list(map(int,input().split()))
ans=10**18
for p in range(1,101):
    ans=min(ans,sum(list(map(lambda x:(p-x)**2,Xlist))))
print(ans)