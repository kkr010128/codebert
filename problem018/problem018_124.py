data = input().split()
operator = ["+", "*", "-"]
stack = []
for x in data:
    if x in operator:
        a = stack.pop()
        b = stack.pop()
        stack.append(str(eval(b + x + a)))
    else:
        stack.append(x)
print(stack[0])