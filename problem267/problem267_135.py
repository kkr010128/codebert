import sys
import math

#https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

N = ini()
S = input()

ans = 0
for i in range(1000):
    V = str(i).zfill(3)
    p1 = S.find(V[0])
    if p1 != -1:
        p2 = S.find(V[1], p1+1)
        if p2 != -1:
            p3 = S.find(V[2], p2+1)
            if p3 != -1:
                ans += 1

print(ans)


