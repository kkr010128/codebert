
A, B, C = map(int,input().split())
if A == B and B != C:
  print('Yes')
elif C == B and C != A:
  print('Yes')
elif A == C and C != B:
  print('Yes')
else:
  print('No')