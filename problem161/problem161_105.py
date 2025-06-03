import math
a,b,n=map(int,input().split())
def f(x):
  return math.floor(a*x/b)-a*(math.floor(x/b))


if n>=(b-1):
  print(f(b-1))
else:
  print(f(n))