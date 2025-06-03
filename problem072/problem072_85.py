n = int(input())
cou = 0
ans = False
for i in range(n):
	da, db = map(int, input().split())
	if da == db:
		cou += 1
	else:
		cou = 0
	if cou == 3:
		ans = True

if ans:
	print('Yes')
else:
	print('No')