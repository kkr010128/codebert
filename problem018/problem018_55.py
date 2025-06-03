operand = ["+", "-", "*"]
src = [x if x in operand else int(x) for x in  input().split(" ")]
stack = []

for s in src:
    if isinstance(s, int):
        stack.append(s)
        continue

    b, a = stack.pop(), stack.pop()

    if s == "+":
       stack.append(a+b)
    elif s == "-":
        stack.append(a-b)
    elif s == "*":
        stack.append(a*b)

print(stack[0])