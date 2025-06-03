n=int(input())
a=list(map(int,input().split()))
ans,tmp=0,1
for i in range(n):
    if a[i]!=tmp: ans+=1
    else: tmp+=1
if ans==n: print(-1)
else: print(ans)