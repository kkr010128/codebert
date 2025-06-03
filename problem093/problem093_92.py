def main():
    INF = 10**9
    n,k = map(int,input().split())
    P = [0] + list(map(int,input().split()))
    C = [0] + list(map(int,input().split()))

    scores = [0]*n

    for s in range(1,n+1):
        start = s
        dp = [-INF]*(n+1)
        dp[0] = 0
        for i in range(n):
            p = P[s]
            dp[i+1] = dp[i] + C[p]
            
            if start == p:
                break
            s = p
        if k <= i+1:
            scores[start-1] = max(dp[1:k+1])
        elif dp[i+1]<=0:
            scores[start-1] = max(dp[1:])
        else:
            r = k%(i+1)
            q = k//(i+1)
            if r>0:
                scores[start-1] = max(max(dp[1:r+1])+dp[i+1]*q, max(dp[1:]))
            else:
                scores[start-1] = dp[i+1]*(q-1)+max(dp[1:])

    print(max(scores))
main()