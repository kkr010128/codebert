a,b,c= (int(x) for x in input().split())
A = int(a)
B = int(b)
C = int(c)

if A+B+C >= 22:
  print("bust")
else:
  print("win")