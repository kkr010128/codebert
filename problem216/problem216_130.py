a,b,c=input().split()
if a==b and a!=c:
  print("Yes")
elif a==c and a!=b:
  print("Yes")
elif b==c and a!=b:
  print("Yes")
else:
  print("No")