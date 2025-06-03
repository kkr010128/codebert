# coding: utf-8

stack = []

f = input().split()

for s in f:
    if s in ('+', '-', '*'):
        stack.append(str(eval("{1}{2}{0}".format(stack.pop(), stack.pop(), s))))
    else:
        stack.append(s)

print(*stack)