s = input()
val = s.split(" ")
a = int(val[0])
b = int(val[1])
if a<b:
  print("a < b")
elif a==b:
  print("a == b")
else:
  print("a > b")