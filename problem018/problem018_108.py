f = list(input().split())
stack = []

for op in f:
    if op in '+-*':
        b = stack.pop()
        a = stack.pop()
        stack.append(str(eval(a+op+b)))
    else:
        stack.append(op)

print(''.join(stack))
