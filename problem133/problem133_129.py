a,b=input().split()
a=int(a)
b=int(float(b)*100)
if (a*b<100):
  print(0)
else:
  print(str(a*b)[:-2])