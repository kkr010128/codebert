import sys
input = sys.stdin.readline
from collections import Counter, defaultdict


def read():
    H, W, M = map(int, input().strip().split())
    HW = []
    for i in range(M):
        h, w = map(int, input().strip().split())
        HW.append((h, w))
    return H, W, M, HW


def solve(H, W, M, HW):
    hcount = Counter()
    wcount = Counter()
    for h, w in HW:
        hcount[h] += 1
        wcount[w] += 1
    hm = hcount.most_common()
    wm = wcount.most_common()
    hmax = hm[0][1]
    wmax = wm[0][1]
    hn = len([1 for k, v in hcount.items() if v == hmax])
    wn = len([1 for k, v in wcount.items() if v == wmax])
    m = hn * wn
    for h, w in HW:
        if hcount[h] == hmax and wcount[w] == wmax:
            m -= 1
    if m == 0:
        return hmax + wmax - 1
    return hmax + wmax


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
