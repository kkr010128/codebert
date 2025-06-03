def max2(x,y):
    return x if x > y else y
N = int(input())
D = []
for i, a in enumerate(map(int, input().split())):
    D.append((a<<11) + i)
D.sort(reverse=True)
dp = [0]*(N+1)
for i, d in enumerate(D,start=1):
    x, a = d%(1<<11),d>>11
    for j in reversed(range(0, i+1)):
        dp[j] = max2((dp[j-1]+a*(x-(j-1)))*(j-1>=0), (dp[j]+a*(N-(i-j)-x))*(j<=i-1))
print(max(dp))