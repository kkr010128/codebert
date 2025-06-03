a,b,c = list(map(int,input().split()))
d = c-a-b
if d <= 0:
  print("No")
else:
  if d**2 > 4*a*b:
    print("Yes")
  else:
    print("No")