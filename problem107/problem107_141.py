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
    W = 16
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
        dc[k] = (x, v, y)

    ans = []
    for i, si in enumerate(S):
        cnt, v, n = dc[si]

        if cnt == 0:
            ans.append(0)
            continue

        ni = N - i - 1
        n = (n + v * pow(2, ni, cnt)) % cnt

        ans.append(1+f2(n))

    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()
