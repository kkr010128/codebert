symbol = list(input().split())
stack = []

while len(symbol) > 0:
    x = symbol.pop(0)
    if x.isdigit():
        stack.append(int(x))
    else:
        a,b = stack.pop(),stack.pop()
        if x == "+":
            stack.append(b + a)
        elif x == "-":
            stack.append(b - a)
        elif x == "*":
            stack.append(b * a)

print(stack.pop())

