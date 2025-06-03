import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, L = map(int, readline().split())
    G = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, readline().split())
        G[a - 1][b - 1] = G[b - 1][a - 1] = c
    for i in range(N):
        G[i][i] = 0

    Q, *ST = map(int, read().split())

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]

    H = [[INF] * N for _ in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if G[i][j] <= L:
                H[i][j] = H[j][i] = 1

    for i in range(N):
        H[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if H[i][j] > H[i][k] + H[k][j]:
                    H[i][j] = H[i][k] + H[k][j]

    ans = [0] * Q
    for i, (s, t) in enumerate(zip(*[iter(ST)] * 2)):
        s -= 1
        t -= 1
        if H[s][t] == INF:
            ans[i] = -1
        else:
            ans[i] = H[s][t] - 1

    print(*ans, sep='\n')
    return


if __name__ == '__main__':
    main()
