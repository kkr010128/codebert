while True:
	a= map(int,raw_input().split())
	if a[0]==0 and a[1]==0:
		break
	a.sort()
	print a[0],a[1]