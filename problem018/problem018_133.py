def reverse_polish_notation(A):
	ops = {'+': lambda a, b: b + a,
	       '-': lambda a, b: b - a,
	       '*': lambda a, b: b * a}

	stack = []

	for i in A:
		if i in ops:
			stack.append(ops[i](stack.pop(), stack.pop()))
		else:
			stack.append(int(i))

	return stack[0]

if __name__ == '__main__':
	A = list(input().split())
	print(reverse_polish_notation(A))