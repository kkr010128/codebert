s = input().split()
stack = []
for v in s:
    # print("v", v)
    # print("stack", stack)
    if v in ["+", "-", "*"]:
        v1 = stack.pop()
        v2 = stack.pop()
        statement = v2 + v + v1
        r = eval(statement)
        stack.append(str(r))
    else:
        stack.append(v)

assert len(stack) == 1
print(stack[0])
