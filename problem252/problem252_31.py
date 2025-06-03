from itertools import accumulate
from bisect import *
n, m, *a = map(int, open(0).read().split())
a = [-x for x in a]
a.sort()
acc = list(accumulate(a)) + [0]
l = 0
r = 2 * 10 ** 5 + 1
while r - l > 1:
	mid = (l + r) // 2
	border = n - 1
	cnt = 0
	for x in a:
		while x + a[border] > -mid:
			border -= 1
			if border < 0:
				break
		if border < 0:
			break
		cnt += border + 1
		if cnt >= m:
			break
	if cnt >= m:
		l = mid
	else:
		r = mid
ans = tot = 0
for x in a:
	b = bisect(a, -l - x)
	tot += b
	ans += acc[b - 1] + x * b
ans += l * (tot - m)
print(-ans)
