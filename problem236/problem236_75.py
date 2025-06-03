a=int(input())
b=int(input())
c=int(input())
if a<b:
  a,b=b,a
if c%a==0:
  print(c//a)
else:
  print(c//a+1)

