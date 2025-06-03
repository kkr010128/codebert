l = []
while True:
  a,op,b = input().split()
  if op == '?':
    break
  A = int(a)
  B = int(b)
  if op == '+':
    l.append(A+B)
  elif op == '-':
    l.append(A-B)
  elif op == '*':
    l.append(A*B)
  elif op == '/':
    l.append(A//B)
for i in l:
  print(i)