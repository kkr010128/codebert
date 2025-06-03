import sys
import bisect
import itertools


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    a.sort()

    cor_v = -1
    inc_v = a[-1] * 2 + 1
    while - cor_v + inc_v > 1:
        bin_v = (cor_v + inc_v) // 2
        cost = 0
        #条件を満たすcostを全検索
        p = n
        for v in a:
            p = bisect.bisect_left(a, bin_v - v, 0, p)
            cost += n - p
            if cost > m:
                break
        #costが制約を満たすか
        if cost >= m:
            cor_v = bin_v
        else:
            inc_v = bin_v
    acm = [0] + list(itertools.accumulate(a))
    c = 0
    t = 0
    for v in a:
        p = bisect.bisect_left(a, cor_v - v)
        c += n - p
        t += acm[-1] - acm[p] + v * (n - p)
    print(t - (c - m) * cor_v)


if __name__ == '__main__':
    solve()
