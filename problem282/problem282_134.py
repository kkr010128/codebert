import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, T = map(int, input().split())
    cv = [tuple(map(int, input().split())) for _ in range(N)]
    dp1 = [[0]*(T+1) for _ in range(N+2)] # [0, i]
    dp2 = [[0]*(T+1) for _ in range(N+2)] # [i, N]

    # 貰うdp
    for i in range(N):
        cost, value = cv[i]

        # dp1
        for now in range(min(T+1, cost)):
            dp1[i+1][now] = dp1[i][now]

        for now in range(cost, T+1):
            old = now - cost
            dp1[i+1][now] = max(dp1[i][now], dp1[i][old] + value)

        # dp2
        cost, value = cv[(N-i)-1]
        for now in range(min(T+1, cost)):
            dp2[N-i][now] = dp2[N-(i-1)][now]

        for now in range(cost, T+1):
            old = now - cost
            dp2[N-i][now] = max(dp2[N-(i-1)][now], dp2[N-(i-1)][old] + value)
    
    ans = 0
    for i in range(1, N+1):
        i_value = cv[i-1][1]
        i_max = max([dp1[i-1][j] + dp2[i+1][(T-1)-j] + i_value for j in range(T)])
        ans = max(ans, i_max)
    print(ans)


    

if __name__ == "__main__":
    main()