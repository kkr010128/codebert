import sys

n=int(input())
c=False


for i in range(n,100000000):
  c=False
  
  for j in range(2,i):
    if i%j==0:
      c=True
      continue
     
  if c==True:
    continue
    
  else:
    print(i)
    sys.exit()