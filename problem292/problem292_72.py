import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    d = list(map(int, input().split()))

    comb = list(itertools.combinations(range(N), 2))
    ans = 0
    for c in comb:
        i1, i2 = c
        ans += d[i1] * d[i2]

    print(ans)


if __name__ == '__main__':
    solve()
