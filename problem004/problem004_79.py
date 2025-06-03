N = int(input())
for _ in range(N):
	a = sorted(map(int, input().split()))
	if a[2]**2 == a[0]**2 + a[1]**2:
		print("YES")
	else:
		print("NO")