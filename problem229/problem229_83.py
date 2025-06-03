def solve():
    H,N = map(int,input().split())
    ap = []
    mp = []

    for _ in range(N):
        a,b = map(int,input().split())
        ap.append(a)
        mp.append(b)
    
    ap_max = max(ap)
    
    dp = [[float('inf')] * (H+ap_max+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 0
    
    for i in range(N):
        for sum_h in range(H+ap_max+1):
            if sum_h - ap[i] >= 0:
                dp[i+1][sum_h] = min(dp[i][sum_h-ap[i]] + mp[i], dp[i][sum_h])
                dp[i+1][sum_h] = min(dp[i+1][sum_h-ap[i]] + mp[i], dp[i][sum_h])
            dp[i+1][sum_h] = min(dp[i+1][sum_h], dp[i][sum_h])
    
    ans = float('inf')
    for sum_h in range(H, H+ap_max+1):
        ans = min(ans,dp[N][sum_h])

    print(ans)

if __name__ == '__main__':
    solve()