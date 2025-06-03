s = raw_input().split()

stack = []
for op in s:
	if op.isdigit():
		stack.append(op)
	else:
		b = int(stack.pop())
		a = int(stack.pop())
		ret = 0
		if op == "+":
			ret = a + b
		elif op == "-":
			ret = a - b
		elif op == "*":
			ret = a * b
		stack.append(str(ret))
print stack.pop()