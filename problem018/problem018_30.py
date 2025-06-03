a=input().split()
operator={
  '+':(lambda x,y:x+y),
  '-':(lambda x,y:x-y),
  '*':(lambda x,y:x*y),
  '/':(lambda x,y:float(x)/y)
}
stack=[]
for i,j in enumerate(a):
  if j not in operator.keys():
    stack.append(int(j))
    continue
  y=stack.pop()
  x=stack.pop()
  stack.append(operator[j](x,y))
print(stack[0])
    
  
