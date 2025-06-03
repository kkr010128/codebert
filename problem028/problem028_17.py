import sys

if __name__ == "__main__":
    n,m = map(int,input().split())
    c = list(map(int,input().split()))
    INF = 10**18
    dp = [INF]*(n+1)
    dp[0] = 0
    for i in c:
        for j in range(i,n+1):
            dp[j] = min(dp[j],dp[j-i]+1)
    print(dp[-1])
