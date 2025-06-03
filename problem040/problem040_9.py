a,b,c = map(int,raw_input().split())
if b <= a:
	if b <= c <= a:
		print b,c,a
	elif c <= b:
		print c,b,a
	else:
		print b,a,c
elif a < b:
	if a <= c <= b:
		print a,c,b
	elif c <= a < b:
		print c,a,b
	else:
		print a,b,c
 