import sys
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    a = list(map(int, readline().split()))
    d = collections.defaultdict(int)
    d[-1] = 3
    mt = 1
    for v in a:
        mt *= d[v-1]
        mt %= mod
        d[v-1] -= 1
        d[v] += 1
    print(mt)


if __name__ == '__main__':
    solve()
