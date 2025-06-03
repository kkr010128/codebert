import sys

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if (a1-b1)*t1+(a2-b2)*t2 == 0:
  print("infinity")
  sys.exit()

e1 = (a1-b1)*t1
e2 = e1 + (a2-b2)*t2

if e1*e2 > 0:
  print(0)
  sys.exit()

e1, e2 = abs(e1), abs(e2)

if e1%e2:
  print(1+2*(e1//e2))
else:
  print(2*(e1//e2))