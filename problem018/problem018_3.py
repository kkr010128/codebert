data = raw_input().split()
#figure = [chr(i) for i in range(ord('0'), ord('9')+1)]

stack = []

for i in range(len(data)):
	if data[i] == "+":
		stack[-2] = stack[-2] + stack[-1]
		del stack[-1]
		#print stack
	elif data[i] == "-":
		stack[-2] = stack[-2] - stack[-1]
		del stack[-1]
		#print stack
	elif data[i] == "*":
		stack[-2] = stack[-2] * stack[-1]
		del stack[-1]
		#print stack
	else:
		stack.append(int(data[i]))
		#print stack

print stack[0]