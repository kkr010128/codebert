a,b=input().split()
a=int(a)
b=int(b)
e=a
d=b
c=1
if a>b:
  for i in range(1,e):
    if a%(e-i)==0 and b%(e-i)==0:
      a=a/(e-i)
      b=b/(e-i)
      c=c*(e-i)
  print(int(a*b*c))
if a<b:
  for i in range(1,d):
    if a%(d-i)==0 and b%(d-i)==0:
      a=a/(d-i)
      b=b/(d-i)
      c=c*(d-i)
  print(int(a*b*c))