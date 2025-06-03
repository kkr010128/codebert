#coding: UTF-8

while True:

	l = raw_input().split()

	a = int(l[0])
	b = int(l[2])

	op =l[1]



	if op == "+":
		x = a + b
		print x

	if op == "-":
		x = a - b
		print x

	if op == "*":
		x = a * b
		print x

	if op == "/":
		x = a / b
		print "%d" %x


	if op == "?":
		break