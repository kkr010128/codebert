# -*- coding: utf-8 -*-


a = [e for e in input().split()]
# a = ['1', '2', '+', '3', '4','-', '*']
# a = ['1', '2', '+']
l = []


for x in a:

    if x not in ['+', '-', '*']:
        x = int(x)
        l.append(x)
    else:
        a = l.pop()
        b = l.pop()

        if x == '+':
            l.append(b + a)
        elif x == '-':
            l.append(b - a)
        elif x == '*':
            l.append(b * a)


print(sum(l))