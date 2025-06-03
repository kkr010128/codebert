import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *L = map(int, read().split())

    L.sort()

    max_L = max(L)

    C = [0] * (max_L + 1)
    for l in L:
        C[l] += 1
    C = list(accumulate(C))

    ans = 0
    for i, a in enumerate(L):
        for j, b in enumerate(L[i + 1 :], i + 1):
            if a + b > max_L:
                ans += N - j - 1
            else:
                ans += C[a + b - 1] - j - 1

    print(ans)
    return


if __name__ == '__main__':
    main()
