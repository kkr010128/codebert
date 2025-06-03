while 1:
	x = raw_input().split()
	a,op,b = int(x[0]),x[1],int(x[2])
	if op == "+":
		print a+b
	elif op == "-":
		print a-b
	elif op == "/":
		print a/b
	elif op == "*":
		print a*b
	else:
		break