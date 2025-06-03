h,a=map(int,input().split())
if h%a!=0:
  n=int(h/a)+1
  print(n)
else:
  n=int(h/a)
  print(n)