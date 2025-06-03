
strN = input()
s = 0
for c in strN:
  s += int(c)

if s % 9 == 0:
  print("Yes")
else:
  print("No")