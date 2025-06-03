import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, s = int(input()), list(map(int, input().split()))
res = [0 for i in range(n)]
for i in range(n): res[s[i]-1] = i + 1
print(' '.join(str(i) for i in res))