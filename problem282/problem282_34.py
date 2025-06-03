
def main():
    N, T = map(int,input().split())
    A = [0]
    B = [0]

    for _ in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)

    dp1 = [[0] * (T + 1) for i in range(N + 1)]
    # dp1[i][t] = 1~i番目から選んでt分以内に食べるときの美味しさの和の最大値
    dp2 = [[0] * (T + 1) for i in range(N + 2)]
    # dp2[i][t] = i~N番目から選んでt分以内に食べるときの美味しさの和の最大値

    for i in range(1, N+1):
        for t in range(T+1):
            if t >= A[i]:
                dp1[i][t] = max(dp1[i-1][t], dp1[i-1][t-A[i]] + B[i])
            else:
                dp1[i][t] = dp1[i-1][t]

    for i in range(N, 0, -1):
        for t in range(T + 1):
            if t >= A[i]:
                dp2[i][t] = max(dp2[i + 1][t], dp2[i + 1][t - A[i]] + B[i])
            else:
                dp2[i][t] = dp2[i + 1][t]

    ans = dp1[N][T]
    for i in range(1, N+1): # 最後にi番目の料理を食べる
        for t in range(T):
            ans = max(ans, dp1[i-1][t] + dp2[i+1][T-1-t] + B[i])
    print(ans)

if __name__ == "__main__":
    main()

