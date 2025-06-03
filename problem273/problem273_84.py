from collections import defaultdict
n, k = map(int, input().split())

a = list(map(lambda x: int(x) - 1, input().split()))
s = [0] * (n + 1)
for i in range(n):
	s[i + 1] = (s[i] + a[i]) % k

mp = defaultdict(int)

ans = 0
for i in range(n + 1):
	ans += mp[s[i]]
	mp[s[i]] += 1
	if i >= k - 1:
		mp[s[i - k + 1]] -= 1
print(ans)
