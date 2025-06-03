x = int(input())

b = int(x/1.08)
x1 = int(b*1.08)
x2 = int((b+1)*1.08)

if x1 == x:
  print(b)
elif x2 == x:
  print(b+1)
else:
  print(":(")