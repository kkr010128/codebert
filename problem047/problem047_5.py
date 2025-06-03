while True:
	a,op,b=input().split(" ")
	a,b=[int(i) for i in (a,b)]
	if op=="+":
		print(a+b)
	elif op=="-":
		print(a-b)
	elif op=="*":
		print(a*b)
	elif op=="/":
		print(int(a/b))
	else:
		break