H, M = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
  H -= i
if H < 0:
  print("-1")
else:
  print(H)