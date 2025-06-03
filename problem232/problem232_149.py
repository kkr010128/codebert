A,B = map(int, input().split())
A1,B1 = str(A), str(B)
A2 = int(str(A)*B)
B2 = int(str(B)*A)
if A2 >= B2:
  print(A2)
else:
  print(B2)