X, Y =map(int,input().split())
a = 0
for i in range(X+1):
  if 2*i+4*(X-i)==Y:
    print('Yes')
  else:
    a +=1
  
    
if a ==X+1:
  print('No')