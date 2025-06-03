import sys; input = sys.stdin.readline
from math import ceil
d, t, s = map(int, input().split())
u, l = ceil(d/t), d//t
if u == l:
    if u <= s: print("Yes")
    else: print("No")
else:
    if d/t <= s: print("Yes")
    else:print("No")