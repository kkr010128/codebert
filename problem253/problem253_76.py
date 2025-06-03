n,a,b = map(int,input().split())

if (b-a) % 2 == 0:
	ans = (b-a) // 2
else:
	if a-1 < n-b:
		ans = b-1
		x = b-(a-1)-1
		ans = min(ans, a + (x-1) // 2)
	else:
		ans = n-a
		x = a + (n-b) + 1
		ans = min(ans, (n-b) + 1 + (n-x) // 2)

print(ans)
