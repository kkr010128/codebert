a, b, c = map(int, input().split())
i = a
ans = 0
while i <= b:
	if c % i == 0:
		ans += 1
	i += 1
print(ans)

