import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, T = map(int, input().split())
    cv = [tuple(map(int, input().split())) for _ in range(N)]
    cv = sorted(cv, key=lambda x : x[0])
    dp = [[0]*(T+1) for _ in range(N+1)]

    # 貰うdp

    ans = 0
    for i in range(N):
        cost, value = cv[i]
        for now in range(min(T+1, cost)):
            dp[i+1][now] = dp[i][now]

        for now in range(cost, T+1):
            old = now - cost
            dp[i+1][now] = max(dp[i][now], dp[i][old] + value)
        
        ans = max(ans, dp[i][T-1] + value)

    print(ans)

if __name__ == "__main__":
    main()