# -*- coding: utf-8 -*-


input_list = input().split()
stack = list()
for i in input_list:
    if i.isdigit():
        stack.append(int(i))
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
print(stack.pop())