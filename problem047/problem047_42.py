while True:
  l = input().split()
  
  a = int(l[0])
  o = l[1]
  b = int(l[2])
  
  if o =='?':
    break
 
  if o == '+':
    print( '%d'%(a+b))
  elif o == '-':
    print('%d'%(a-b))
  elif o =='*':
    print('%d'%(a*b))
  else:
    o =='/'
    print('%d'%(a//b))
