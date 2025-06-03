a = int(input())
b = a // 100
c = a // 10 - b * 10
d = a - b * 100 - c * 10
if b != 7 and c != 7 and d != 7:
  print("No")
else:
  print("Yes")