n, k = map(int, input().split())
a = [(int(i) + 1)/2 for i in input().split()]
ans = 0
s = sum(a[:k])
ans = s
for i in range(k, n):
	s -= a[i - k]
	s += a[i]
	ans = max(ans, s)
print(ans)