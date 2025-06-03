import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T, *AB = map(int, read().split())
    A = AB[::2]
    B = AB[1::2]

    dp1 = [[0] * T for _ in range(N + 1)]
    for i in range(N):
        for t in range(T):
            if 0 <= t - A[i]:
                dp1[i + 1][t] = dp1[i][t - A[i]] + B[i]
            if dp1[i + 1][t] < dp1[i][t]:
                dp1[i + 1][t] = dp1[i][t]

    dp2 = [[0] * T for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for t in range(T):
            if 0 <= t - A[i]:
                dp2[i][t] = dp2[i + 1][t - A[i]] + B[i]
            if dp2[i][t] < dp2[i + 1][t]:
                dp2[i][t] = dp2[i + 1][t]

    ans = 0
    for i in range(N):
        tmp = max(dp1[i][t] + dp2[i + 1][T - t - 1] for t in range(T)) + B[i]
        if ans < tmp:
            ans = tmp

    print(ans)
    return


if __name__ == '__main__':
    main()
