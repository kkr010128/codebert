import sys
d = -float('inf')
n = int(input())
l = int(input())
for s in sys.stdin:
	r = int(s)
	d = max(d, r-l)
	l = min(l, r)
print(d)
