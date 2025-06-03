a,b=input().split()
a=int(a)
b=int(b)
if a%b==0:
  print(int(a/b))
else:
  print(int((a/b)+1))