l = input().split()
stack = []
for op in l:
    if op.isdigit():
        stack.append(int(op))
    elif op == '+':
        stack.append(stack.pop() + stack.pop())
    elif op == '-':
        stack.append(- stack.pop() + stack.pop())
    elif op == '*':
        stack.append(stack.pop() * stack.pop())
print(stack[-1])