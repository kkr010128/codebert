import sys

inf = 1<<30

def solve():
    n, m = map(int, input().split())
    c = [int(i) for i in input().split()]
    c.sort()

    dp = [inf] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for cj in c:
            if i - cj < 0:
                break
            dp[i] = min(dp[i], dp[i - cj] + 1)

    ans = dp[n]
    print(ans)

if __name__ == '__main__':
    solve()