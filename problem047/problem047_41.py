def cal(a, op, b):

  if op == '+':
    r = a + b
  elif op == '-':
    r = a - b
  elif op == '*':
    r = a * b
  else:
    r = a / b
  return r

while 1:
  a,op,b = raw_input().split()
  if op == '?':
    break
  else:
    print(cal(int(a), op, int(b)))