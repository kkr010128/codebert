a = raw_input().split()
while a[1] != '?':
	print eval(a[0]+a[1]+a[2])
	a = raw_input().split()