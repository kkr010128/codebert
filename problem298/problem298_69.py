N,K=map(int, input().split())
d=list(map(int,input().split()))
ans=0
for i in range(N):
    if d[i]>=K:
        ans=ans+1
print(ans)