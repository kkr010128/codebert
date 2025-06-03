# -*- coding:utf-8 -*-

stack = list()

def deal_expression(x):
    if x.isdigit():
        stack.append(int(x))
    else:
        a = stack.pop()
        b = stack.pop()
        if x == '+':
            stack.append(b + a)
        elif x == '-':
            stack.append(b - a)
        elif x == '*':
            stack.append(b * a)
        elif x == '/':
            stack.append(b / a)

for x in input().split():
    deal_expression(x)
print(stack[0])