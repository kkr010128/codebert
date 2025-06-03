T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 < B1:
  A1, A2, B1, B2 = B1, B2, A1, A2

xa = A1*T1 + A2*T2
xb = B1*T1 + B2*T2
if xa > xb:
  print(0)
elif xa == xb:
  print('infinity')
else:
  d1 = (A1 - B1) * T1
  d2 = xb - xa
  n = d1 // d2
  if d1 % d2 == 0:
    print(2*n)
  else:
    print(2*n + 1)
