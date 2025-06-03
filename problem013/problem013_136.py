f = lambda: int(input())
d = -float('inf')
n = f()
l = f()
for _ in range(n-1):
	r = f()
	d = max(d, r-l)
	l = min(l, r)
print(d)
