ts = input().split(" ")
stack = []
for t in ts:
    if t not in ("-", "+", "*"):
        stack.append(int(t))
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if t == "-":
            stack.append(n1 - n2)
        elif t == "+":
            stack.append(n1 + n2)
        else:
            stack.append(n1 * n2)
print(stack.pop())