import sys
input = sys.stdin.readline
from collections import defaultdict

(n, m), d, a, b = map(int, input().split()), defaultdict(int), 0, 0
for i in range(m):
	p, s = input()[:-1].split(); p = int(p)
	if d[p] == sys.maxsize: continue
	if s == 'WA': d[p] += 1
	if s == 'AC': b += abs(d[p]); a += 1; d[p] = sys.maxsize
print(a, b)