for _ in range(int(input())):
	a=list(map(int,input().split()))
	a.sort()
	print("YES") if a[0]**2+a[1]**2==a[2]**2 else print("NO")