
def main():
    inf = 1<<29
    n,m = map(int,input().split())
    coins = list(map(int,input().split()))
    dp = [inf]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i-coins[j]<0:continue
            dp[i] = min(dp[i],dp[i-coins[j]]+1)
    print (dp[n])


if __name__ == '__main__':
    main()


