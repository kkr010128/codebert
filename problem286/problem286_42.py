A,B = map(int, input().split())
if A > 9 or B > 9 or A < 1 or B < 1:
  print(-1)
else:
  print(A*B)