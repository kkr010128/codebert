import sys
s_max = -float('inf')
s = 0
n = int(input())
r = list(map(int, sys.stdin.read().split()))
for i in range(1, n):
	s = max(s, 0) + r[i] - r[i-1]
	s_max = max(s, s_max)
print(s_max)
