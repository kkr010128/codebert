while True:
	s = input().rstrip().split(' ')
	a = int(s[0])
	b = int(s[2])
	op = s[1]
	if op == "?":
		break
	elif op == "+":
		print(str(a + b))
	elif op == "-":
		print(str(a - b))
	elif op == "*":
		print(str(a * b))
	elif op == "/":
		print(str(int(a / b)))