N=int(input())
 
flag=0
for i in range(1,10):
  for j in range(1,10):
    if N==i*j:
      flag+=1
 
if flag==0:
  print('No')
else:
  print('Yes')
