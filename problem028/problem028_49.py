import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M = map(int, readline().split())
    C = list(map(int, readline().split()))
    # dp[i] := i円払うのに必要な枚数
    dp = [INF] * (N+1)
    dp[0] = 0
    for c in C:
        if c<=N:
            for i in range(N-c+1):
                dp[i+c] = min(dp[i]+1, dp[i+c])
    print(dp[N])


if __name__ == '__main__':
    main()


