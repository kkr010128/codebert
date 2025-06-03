V = input()
s = 0
for c in V:
  n = int(c)
  s = s + n
  
if s%9 == 0:
  print("Yes")
else:
  print("No")