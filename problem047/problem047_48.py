op = "$"

while op != "?":
	a, op, c = map(str, raw_input().split())
	a = int(a)
	c = int(c)

	if   op == "+":
		print u"%d" % (a+c)
	elif op == "-":
		print u"%d" % (a-c)
	elif op == "*":
		print u"%d" % (a*c)
	elif op == "/":
		print u"%d" % (a/c)
	else:
		break