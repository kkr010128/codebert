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
    for i in range(N):
        a = L[i]
        for j in range(i + 1, N):
            b = L[j]
            left = bisect_left(L, b, lo=j + 1)
            right = bisect_left(L, a + b, lo=j + 1)
            ans += right - left

    print(ans)
    return


if __name__ == '__main__':
    main()
