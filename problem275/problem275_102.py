a = {1:300000,2:200000,3:100000}

x,y = map(int,input().split())

if x == 1 and y == 1:
	print(a[x] + a[y] + 400000)
else:
	if x > 3 and y <= 3:
		print(a[y])
	elif x <= 3 and y > 3:
		print(a[x])
	elif x>3 and y >3:
		print(0)
	else:
		print(a[x] + a[y])