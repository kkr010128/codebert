n,x,t = map(int, input().split())
 
if n <= x:
  print(t)
elif n % x == 0:
  print(n//x*t)
else:
  print((n//x+1)*t)