import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    dp = [[0] * 10 for _ in range(10)]

    ans = 0
    for i in range(1, N + 1):
        s = str(i)
        first = int(s[0])
        second = int(s[-1])

        ans += 2 * dp[second][first]

        if first == second:
            ans += 1

        dp[first][second] += 1

    print(ans)


if __name__ == '__main__':
    main()
