s = input().split()

stack = []

for a in s:
    if a == '+':
        stack.append(stack.pop() + stack.pop())
    elif a == '-':
        stack.append(-(stack.pop() - stack.pop()))
    elif a == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(a))

print(stack[0])