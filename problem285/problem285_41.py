s = input()
n = len(s)
dp = [0]*(n+1)
t = 0
for e,i in enumerate(s,1):
    if i=='<' :
        dp[e]=dp[e-1]+1
# print(dp)
t = 0
for e in range(n-1,-1,-1):
    i = s[e]
    # print(t)
    if i=='>' :
        dp[e]=max(dp[e],dp[e+1]+1)
# print(dp)
print(sum(dp))