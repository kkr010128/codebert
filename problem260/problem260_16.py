a1, a2, a3 = map(int, input().split(" "))
tmp = a1 + a2 + a3
if tmp >= 22:
  print("bust")
else:
  print("win")