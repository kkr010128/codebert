while True:
	a,b = map(int,raw_input().split())
	if a == 0:
		if b==0:
			break
		elif b>0:
			print a,b
		else:
			print b,a
	elif a>=b:
		print b,a
	else:
		print a,b