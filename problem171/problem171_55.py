N = int(input())
D = []
for i, a in enumerate(map(int, input().split())):
    D.append((a<<11) + i)
D.sort(reverse=True)
dp = [0]*(N+1)
for i, d in enumerate(D,start=1):
    x, a = d%(1<<11),d>>11
    for j in reversed(range(i)):
        dp[j+1] = max(dp[j] + a*(x-j), dp[j+1])
        dp[j] += a*(N-(i-j)-x)
print(max(dp))