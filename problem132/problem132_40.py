import sys
from itertools import accumulate


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(K):
        B = [0 for _ in range(N)]
        count = 0
        for i in range(N):
            if A[i] == N:
                count += 1
            l = max(0, i - A[i])
            r = min(N - 1, i + A[i])
            B[l] += 1
            if r + 1 < N:
                B[r + 1] -= 1
        B = list(accumulate(B))
        if count == N:
            break
        else:
            A = B
    print(*B, sep=" ")


if __name__ == "__main__":
    main()
