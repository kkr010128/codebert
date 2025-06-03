import math
from collections import deque

H, W = [int(_) for _ in input().split()]

S = [list(input()) for _ in range(H)]


def f(h, w):
    memo = [[-1] * W for _ in range(H)]
    lst = deque()
    lst.append((h, w, 0))
    res = 0
    while lst:
        h, w, c = lst.popleft()
        if memo[h][w] >= c: continue
        memo[h][w] = c
        res = max(c, res)
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh = x + h
            nw = y + w
            if nh < 0 or nh >= H: continue
            if nw < 0 or nw >= W: continue
            if memo[nh][nw] > -1: continue
            if S[nh][nw] == '#': continue
            lst.append((nh, nw, c + 1))

    return res

def main():
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#': continue
            ans = max(ans,f(h,w))
    return ans
print(main())

