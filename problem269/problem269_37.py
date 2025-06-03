import sys
input = sys.stdin.readline
T = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = (a[0] - b[0]) * T[0]
q = (a[1] - b[1]) * T[1]

if p > 0:
  p *= -1
  q *= -1
if p + q < 0:
  print(0)
elif p + q > 0:
  print(-p // (p + q) * 2 + ((-p % (p + q)) > 0))
else:
  print("infinity")