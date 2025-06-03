x = input()
s = 0

for i in range(len(x)):
  s = s + int(x[i])

if s % 9 == 0:
  print("Yes")
else:
  print("No")