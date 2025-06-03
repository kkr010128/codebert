# encoding:utf-8

while True:
    a,op,b = map(str, input().split())
    c = int(a)
    d = int(b)
    if op == '+': result = c + d
    if op == '-': result = c - d
    if op == '*': result = c * d
    if op == '/': result = int(c / d)
    if op == '?': break
    print("{0}".format(result))