
while True:
	s = str(input())
	if s == '0': break

	ans = 0
	for c in s:
		ans += int(c)
	print(ans)

