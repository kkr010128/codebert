line = input()
A = line.split()

stack = []

for c in A:
    if c == '+':
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs + rhs)
    elif c == '-':
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs - rhs)
    elif c == '*':
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs * rhs)
    else:
        stack.append(int(c))


print(stack.pop())