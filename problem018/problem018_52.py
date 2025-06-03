
def revPoland(expr):
    stack = []

    for l in expr:
        if l.isdigit():
            stack.append(int(l))
            # print(stack)
        else:
            a = stack.pop()
            b = stack.pop()
            c = eval(str(b) + l + str(a))
            stack.append(c)
            # print(stack)

    return stack.pop()

expr = input().split()

print(revPoland(expr))