k = int(input())
a, b = map(int, input().split())
if a % k == 0:
  print("OK")
  exit()
nex = k * ((a // k) + 1)
if nex <= b:
  print("OK")
else:
  print("NG")