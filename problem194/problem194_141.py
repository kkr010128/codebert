#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)


# adjacent_2
def adjacent_2(h, w, H, W):
    ret = []
    for (dh, dw) in [(0, 1), (1, 0)]:
        h_ = h + dh
        w_ = w + dw
        if (0 <= h_) & (h_ < H) & (0 <= w_) & (w_ < W):
            ret.append((h_, w_))
    return ret


H, W = map(int, readline().split())
A = [list(readline().decode().rstrip()) for _ in range(H)]
cnt = [[1000 for _ in range(W)] for _ in range(H)]

if A[0][0] == '.':
    cnt[0][0] = 0
else:
    cnt[0][0] = 1

for h in range(H):
    for w in range(W):
        acc = adjacent_2(h, w, H, W)
        for h_, w_ in acc:
            if (A[h][w] == ".") & (A[h_][w_] == "#"):
                cnt[h_][w_] = min(cnt[h][w] + 1, cnt[h_][w_])
            else:
                cnt[h_][w_] = min(cnt[h][w], cnt[h_][w_])

print(cnt[H - 1][W - 1])
