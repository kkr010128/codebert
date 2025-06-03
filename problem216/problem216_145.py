import sys
a,b,c=map(int,input().split())
if a==b and b!=c:
  print("Yes")
  sys.exit()
elif c==b and b!=a:
  print("Yes")
  sys.exit()
elif a==c and b!=c:
  print("Yes")
  sys.exit()
else:
  print("No")
  sys.exit()