n = int(input())
x = list(map(int, input().split()))
ans = x[0]
if 0 in x:
	ans = 0
else:
	for i in range(1,n):
		ans = ans * x[i]
		if ans > 10 ** 18:
			ans = -1
			break
print(ans)