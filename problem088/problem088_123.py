from sys import stdin
import math
inp = lambda : stdin.readline().strip()

n = int(inp())
a = [int(x) for x in inp().split()]
ans = 0
for i in range(1, n):
	if a[i] < a[i-1]:
		ans += a[i-1] - a[i]
		a[i] += a[i-1] - a[i]
print(ans)