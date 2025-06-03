# https://atcoder.jp/contests/abc157/tasks/abc157_e

from string import ascii_lowercase
from bisect import bisect_left, insort
from collections import defaultdict

N = int(input())
S = list(input())
Q = int(input())

locs = {c: [] for c in ascii_lowercase}
for i in range(N):
    locs[S[i]].append(i + 1)

for _ in range(Q):
    qt, l, r = input().split()
    l = int(l)
    if int(qt) == 1:
        if S[l - 1] != r:
            locs[S[l - 1]].remove(l)
            S[l - 1] = r
            insort(locs[r], l)
    else:
        count = 0
        r = int(r)
        for ch in ascii_lowercase:
            if len(locs[ch]) > 0:
                left = bisect_left(locs[ch], l)
                if left != len(locs[ch]):
                    if locs[ch][left] <= r:
                        count += 1

        print(count)