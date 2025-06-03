n=int(input())
flag=0
for i in range(1,10):
  if (n%i)==0:
    if (n//i)<=9:
      flag=1
      break
if flag==1:
  print ('Yes')
else:
  print ('No')