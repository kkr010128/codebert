N=int(input())
xl=[list(map(int,input().split()))for _ in range(N)]
rl=[[x+l,x-l]for x,l in xl]
rl.sort()
now=-10**9
ans=0
for r,l in rl:
    if l>=now:
        ans+=1
        now=r
print(ans)