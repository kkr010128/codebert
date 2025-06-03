def repint(n, k):
	if n % k == 0:
		return 0
	res = abs((n % k) - k)
	if (n % k) > res:
		return res
	return (n % k)
n, k = map(int, input().split())
print(repint(n, k))