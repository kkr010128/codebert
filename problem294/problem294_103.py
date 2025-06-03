import sys
from bisect import bisect_left, bisect_right

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *L = map(int, read().split())

    L.sort()

    ans = 0
    for i, a in enumerate(L):
        for j, b in enumerate(L[i + 1 :], i + 1):
            k = bisect_left(L, a + b, lo=j + 1)
            ans += k - j - 1

    print(ans)
    return


if __name__ == '__main__':
    main()
