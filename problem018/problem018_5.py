operand = ["+", "-", "*"]
src = [x if x in operand else int(x) for x in  input().split(" ")]
stack = []

for s in src:
    if isinstance(s, int):
        stack.append(s)
    elif s == "+":
       b, a = stack.pop(), stack.pop()
       stack.append(a+b)

    elif s == "-":
        b, a = stack.pop(), stack.pop()
        stack.append(a-b)
    elif s == "*":
        b, a = stack.pop(), stack.pop()
        stack.append(a*b)

print(stack[0])