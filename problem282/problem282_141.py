import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, T = map(int, input().split())
    cv = [tuple(map(int, input().split())) for _ in range(N)]
    cv = sorted(cv, key=lambda x : x[0])

    dp = [[0]*(T+1) for _ in range(N+1)]
    dp_ext = [[0]*(T+1) for _ in range(N+1)]

    values = [v for c, v in cv]
    max_values = [max(values[i:]) for i in range(N)]
    # 貰うdp
    for i in range(N):
        cost, value = cv[i]
        for now in range(cost, T+1):
            old = now - cost
            dp[i+1][now] = max(dp[i][now], dp[i][old] + value)

        for j in range(1, T+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i+1][j-1])
        
        for j in range(1, T+1):
            dp_ext[i+1][j] = max(dp[i+1][j], dp[i][j-1] + max_values[i], dp_ext[i][j])

    print(dp_ext[N][T])

if __name__ == "__main__":
    main()