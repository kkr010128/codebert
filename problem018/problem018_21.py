# encoding: utf-8

input = raw_input().split()

stack = []
for n in input:
    if(n.isdigit()):
        stack.append(int(n))
    else:
        a = stack.pop()
        b = stack.pop()
        if n == '+':
            stack.append(b + a)
        elif n == '-':
            stack.append(b - a)
        elif n == '*':
            stack.append(b * a)
        else:
            stack.append(b / a)
print stack.pop()