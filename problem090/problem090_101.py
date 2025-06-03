s = input()
ans = 0
a = []

for i in s:
	if i == 'R':
		ans += 1
	else :
		ans = 0
	a.append(ans)
print(max(a)) 