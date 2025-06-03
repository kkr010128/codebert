import sys
import heapq


input = sys.stdin.readline
n, k, s = map(int, input().split())

for i in range(n):
    if i < k:
        print(s)
    else:
        if s >= 10**9:
            print(1)
        else:
            print(s+1)