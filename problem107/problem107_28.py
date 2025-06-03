#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())
from functools import lru_cache


@lru_cache(maxsize=2*10**5)
def f2(x):
    if x == 0: return 0
    y = bin(x).count("1")
    return 1 + f2(x % y)

def resolve():
    N = int(input())
    S = input()
    cnt0 = S.count("1")

    if cnt0 == 0:
        print(*[1]*N, sep="\n")
        return

    X = int(S, 2)

    dc = {}
    for k, v in (("0", 1), ("1", -1)):
        x = cnt0 + v
        y = X % x if x else 0
        dc[k] = (x, v, y, [1, N-1])

    ans = [0] * N
    for i in reversed(range(N)):
        si = S[i]
        cnt, v, n, m1 = dc[si]

        if cnt == 0:
            ans[i] = 0
            continue

        ni = N - i - 1
        m2 = (m1[0]<<(m1[1]-i)) % cnt
        n = (n + v*m2) % cnt
        m1[0] = m2; m1[1] = i

        ans[i] = 1 + f2(n)

    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()
