import itertools


def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = [(A[i], i) for i in range(N)]
    X.sort(reverse=True)
    l = 0
    r = N-1
    ans = 0
    dp = [[0] * (i+1) for i in range(N+1)]
    for i in range(N):
        cost, prev = X[i]
        dp[i+1][0] = dp[i][0] + cost * abs(prev - (N - 1 - i))
        dp[i+1][i+1] = dp[i][i] + cost * abs(prev - i)
        for j in range(1, i+1):
            pos1 = N - 1 - i + j
            pos2 = j - 1
            dp[i+1][j] = max(dp[i][j] + cost * abs(prev - pos1),
                             dp[i][j-1] + cost * abs(prev - pos2))
    print(max(dp[N]))


if __name__ == "__main__":
    main()
