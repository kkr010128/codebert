import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


H, W, M = MI()
h = [0] * H
w = [0] * W
item_list = [[0, 0] for _ in range(M)]

for i in range(M):
    item_h, item_w = MI()
    item_h -= 1
    item_w -= 1
    h[item_h] += 1
    w[item_w] += 1
    item_list[i][0] = item_h
    item_list[i][1] = item_w

h_max = max(h)
w_max = max(w)
h_cnt = h.count(h_max)
w_cnt = w.count(w_max)
ans = h_max + w_max

cnt = 0
for item in item_list:
    if h[item[0]] == h_max and w[item[1]] == w_max:
        cnt += 1

x = h_cnt * w_cnt
if cnt == x:
    ans -= 1

print(ans)
