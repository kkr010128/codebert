inList = input().split()
stack = []
for i in inList:
    if i in ['+', '-', '*']:
        b, a = stack.pop(), stack.pop()
        if i == '+':
            stack.append(b + a)
        if i == '-':
            stack.append(a - b)
        if i == '*':
            stack.append(b * a)
    else:
        stack.append(int(i))
print(stack.pop())