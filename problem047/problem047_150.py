def proc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b
  
while True:
    a, op, b = input().split()
    if op == '?':
        break
    print(proc(int(a), int(b), op))