n = int(input())
s = sorted([int(i) for i in input().split()])
for i, v in enumerate(s[0:-1]):
	if v == s[i+1]:
		print('NO')
		exit()
print('YES')