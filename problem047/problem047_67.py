from sys import stdin

def calc(a, op, b):
    if op == '+':
        return a+b

    if op == '-':
        return a-b

    if op == '*':
        return a*b

    if op == '/':
        return int(a/b)


for line in stdin:
    a, op, b = line.rstrip().split(' ')

    if op == '?':
        break

    print(calc(int(a), op, int(b)))