n=int(input())
a=input()

if n%2!=0:
  print('No')
  exit()

t1=a[0:int(n/2)]
t2=a[int(n/2):n]

if t1==t2:
  print('Yes')
else:
  print('No')