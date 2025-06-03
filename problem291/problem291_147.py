a = input().split()
if int(a[0]) <= int(a[1]) * 2:
  print("0")
else:
  print(int(int(a[0]) - int(a[1]) * 2))