ope = list(input().split())

stack = []

for o in ope:
    if o == '+':
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)
    elif o == '-':
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)
    elif o == '*':
        b, a = stack.pop(), stack.pop()
        stack.append(a * b)
    else:
        stack.append(int(o))

print(stack[0])

