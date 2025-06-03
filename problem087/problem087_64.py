n = list(map(int, list(input())))

while len(n) > 1: 
  tmp = sum(n)
  n = list(map(int, list(str(tmp))))

if n[0] % 9 == 0: 
  print("Yes")
else: 
  print("No")