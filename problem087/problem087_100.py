n = input()
m = 0
for i in range(len(n)):
  m += int(n[i])
  m %= 9
  
if m == 0:
  print("Yes")
else:
  print("No")