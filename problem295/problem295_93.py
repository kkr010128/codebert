import sys
from copy import deepcopy

def main():
    INF = 10**18
    input = sys.stdin.readline
    N, M, L = [int(x) for x in input().split()]
    d = [set() for _ in range(N+1)]
    ds = [[INF] * (N+1) for _ in range(N+1)]
    bs = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        A, B, C = [int(x) for x in input().split()]
        A, B = sorted([A, B])
        d[A].add(B)
        if L >= C:
            ds[A][B] = C

    nes = set()
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                ds[i][j] = min(ds[i][j], ds[min(i, k)][max(i, k)] + ds[min(k, j)][max(k, j)])
                if ds[i][j] <= L:
                    bs[i][j] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                bs[i][j] = min(bs[i][j], bs[min(i, k)][max(i, k)] + bs[min(k, j)][max(k, j)])

    Q, = [int(x) for x in input().split()]
    for _ in range(Q):
        s, t = sorted(int(x) for x in input().split())
        print(bs[s][t]-1 if bs[s][t] < INF else -1)


if __name__ == '__main__':
    main()
