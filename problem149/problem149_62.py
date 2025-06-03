#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    N, M, X = map(int, input().split())
    A = []
    for i in range(N):
        a = [int(x) for x in input().split()]
        A.append(a)

    ans = 10 ** 7
    for bit in range(1 << N):
        res = [0 for _ in [0] * (M + 1)]
        for i in range(N):
            if bit & (1 << i):
                res = [a + b for a, b in zip(res, A[i])]
        if all(a >= X for a in res[1:]):
            ans = min(ans, res[0])
    if ans == 10 ** 7:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
