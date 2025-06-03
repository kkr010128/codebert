import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    dp = [0] * 47
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N])



if __name__ == '__main__':
    main()


