while True:

	a, op, b = map(str, raw_input().split())

	a = int(a)
	b = int(b)

	if op == '+':
		print a + b
	elif op == '-':
		print a - b
	elif op == '*':
		print a * b
	elif op == '/':
		if b != 0:
			print a / b
	elif op == '?':
		break
	else:
		break