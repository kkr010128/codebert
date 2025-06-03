T=int(input())
a=T//1000
T=T-1000*a
if T==0:
  print(0)
else:
  print(1000-T)