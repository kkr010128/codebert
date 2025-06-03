def main():
    h, n = list(map(int, input().split()))
    A, B = [], []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    mx = max(A)
    INF = float('inf')
    dp = [INF] * (h + mx + 1)
    dp[0] = 0
    for i in range(1, h + mx + 1):
        for a, b in zip(A, B):
            if i - a < 0:
                dp[i] = min(dp[i], b)
            else:
                dp[i] = min(dp[i], dp[i - a] + b)
    print(min(dp[h:h + mx + 1]))


if __name__ == '__main__':
    main()
