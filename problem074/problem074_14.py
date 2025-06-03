
def main():
    mod = 998244353
    N, K = map(int,input().split())

    v = []
    for _ in range(K):
        L, R = map(int,input().split())
        # for d in range(L, R+1):
        #     moves.append(d)
        v.append((L, R))
    v.sort()

    dp = [0] * N        # マスi-1に到達するまでの操作列の個数
    sdp = [0] * (N + 1) # dp[i]までの累積和 
    dp[0] = 1
    sdp[1] = 1

    for n in range(1, N):
        for p in v:
            left = max(0, n - p[1])
            right = max(0, n - p[0]+1)
            dp[n] += (sdp[right] - sdp[left]) % mod
        sdp[n+1] = (sdp[n] + dp[n]) % mod

    print(dp[-1] % mod)

if __name__ == "__main__":
    main()

