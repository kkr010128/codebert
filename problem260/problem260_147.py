tmp = input().split(" ")

a = int(tmp[0])
b = int(tmp[1])
c = int(tmp[2])

if a + b + c >= 22:
  print("bust")
else:
  print("win")