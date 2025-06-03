#dp

#dp[T] T分での最大幸福 幸福度B、時間A

N,T = map(int,input().split())

li = [list(map(int,input().split())) for _ in  range(N)]

li = sorted(li,key=lambda x: x[0])

dp = [0]*T
counter = 0
for i in range(N-1):
    A,B = li[i]
    counter = max(counter,max(dp)+B)
    if A>T-1:
        continue
    for t in range(T-A-1,-1,-1):
        dp[t+A]=max(dp[t]+B,dp[t+A])

print(max(max(dp)+li[N-1][1],counter))
