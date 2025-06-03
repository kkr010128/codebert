min2 = lambda x,y: x if x < y else y
H,N = map(int,input().split())


dp = [float('inf')]*(H+1)
dp[0] = 0

for _ in range(N):
    a,b = map(int,input().split())
    for i,v in enumerate(dp):
        j = min2(H,i+a)
        dp[j] = min2(dp[j],v+b)

print(dp[-1])