N=int(input())
A=list(map(int,input().split()))

M=1000050

dp=[0 for i in range(M)]

ans=0
for x in A:
    if dp[x]!=0:
        dp[x]=2
        continue
    for i in range(x,M,x):
        dp[i]+=1

for x in A:
    if dp[x]==1:
        ans+=1

print(ans)
