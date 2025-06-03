a, b, c = map(int, input().split())
p = 4*a*b
q = c-a-b
if q > 0 and q*q > p:
  print("Yes")
else:
  print("No")