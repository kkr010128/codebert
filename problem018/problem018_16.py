def stacker(l):
  stack=[0]
  a=0
  b=0
  for i in l:
    if i=="+":
      a=int(stack[-1])
      b=int(stack[-2])
      stack.pop()
      stack.pop()
      stack.append(a+b)
    elif i=="-":
      a=int(stack[-1])
      b=int(stack[-2])
      stack.pop()
      stack.pop()
      stack.append(-a+b)
    elif i=="*":
      a=int(stack[-1])
      b=int(stack[-2])
      stack.pop()
      stack.pop()
      stack.append(a*b)
    else:
      stack.append(i)
  print(stack[-1])
l=list(input().split())
stacker(l)
