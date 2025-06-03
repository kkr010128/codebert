while 1:
	n = input().split()
	a = int(n[0])
	op = n[1]
	b = int(n[2])
	if op == "?":
		break
	if op == "+":
		print(a+b)
	elif op == "-":
		print(a-b)
	elif op == "*":
		print(a*b)
	elif op == "/":
		print(int(a/b))