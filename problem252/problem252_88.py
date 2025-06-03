from itertools import accumulate
n, m, *a = map(int, open(0).read().split())
a = [-x for x in a]
a.sort()
acc = list(accumulate(a))
l, r = 0, 2 * 10 ** 5 + 1
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
border = n - 1
for x in a:
	while x + a[border] > -l:
		border -= 1
		if border < 0:
			break
	if border < 0:
		break
	ans += acc[border] + x * (border + 1)
	tot += border + 1
ans += l * (tot - m)
print(-ans)