import sys
import copy
from collections import deque
stdin = sys.stdin

mod = 10**9+7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n,k = na()

if n==k-1:
    print(1)
    exit(0)

prev_min = sum([i for i in range(k)])
prev_max = sum([i for i in range(n, n-k, -1)])
prev_num_min = k-1
prev_num_max = n-k+1
cnt = 0
for i in range(n-k+2):
    # print("{} {}".format(prev_min, prev_max))
    cnt += prev_max-prev_min+1
    cnt %= mod
    
    prev_num_min += 1
    prev_num_max -= 1
    prev_min += prev_num_min
    prev_max += prev_num_max

print(cnt)


