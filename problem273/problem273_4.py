import sys
import itertools
import collections


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, input().rstrip('\n').split()))
    ls = [0] + list(map(lambda x: int(x) - 1, input().rstrip('\n').split()))
    ls = [i % k for i in list(itertools.accumulate(ls))]
    
    d = collections.defaultdict(int)
    t = 0
    for i, x in enumerate(ls):
        t += d[x]
        d[x] += 1
        if i >= k - 1:
            d[ls[i - k + 1]] -= 1
    print(t)


if __name__ == '__main__':
    solve()
