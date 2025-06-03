data = list(input().split(" "))
stack = []
for d in data:
    if d == '+':
        stack.append(stack.pop() + stack.pop())
    elif d == '-':
        stack.append(- stack.pop() + stack.pop())
    elif d == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(d))
print(stack[0])