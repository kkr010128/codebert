h=int(input())
w=int(input())
n=int(input())

m=max(h,w)
if n%m==0:
  print(int(n/m))
else:
  print(int(n/m+1))