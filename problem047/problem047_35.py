while True:
  a, op, b = input().split()
  a, b = int(a), int(b)
  if op == '?':
    quit()
  else:
    if op == '+':
      result = a+b
    elif op == '-':
      result = a-b
    elif op == '*':
      result = a*b
    elif op == '/':
      result = int(a/b)
    print(result)