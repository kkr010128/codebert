while True :
  x,op,y = input().split()
  x=int(x)
  y=int(y)
  if op == '?' :
    break
  elif op == '+' :
    print(x+y)
  elif op == '-' :
    print(x-y)
  elif op == '*' :
    print(x*y)
  else :
    print(x//y)
