a,b=input().split()
a=int(a)
b=int(b)
c=list(map(int,input().split()))
c.sort()
if c[-b]>=(sum(c)/(4*b)):
  print("Yes")
else:
  print("No")