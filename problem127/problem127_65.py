X, Y = map(int, input().split())
ans = ''
for i in range(X+1):
	if (i*2 + (X-i)*4) == Y:
		ans = 'Yes'
		break
	else:
		ans = 'No'
print(ans)