a, b, c = map(int,input().split())
if 4*a*b + 2*a*c + 2*b*c < a**2 + b**2 + c**2+ 2*a*b and c-a-b>0:
  print("Yes")
else:
  print("No")