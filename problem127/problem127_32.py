a,b=map(int,input().split())
c=0
for i in range (0,a+1):
  for j in range (0,a+1):
    if (i+j)==a and (i*2 + j *4) == b:
      c+=1
if c== 0:
  print('No')
else:
  print('Yes')