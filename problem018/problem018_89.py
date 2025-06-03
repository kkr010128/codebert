ops = [op for op in input().split(" ")]
stack = []
for op in ops:
    if op == "+":
        stack = stack[:-2]+[stack[-2]+stack[-1]]
    elif op == "-":
        stack = stack[:-2]+[stack[-2]-stack[-1]]
    elif op == "*":
        stack = stack[:-2]+[stack[-2]*stack[-1]]
    else:
        stack.append(int(op))
print(stack[0])