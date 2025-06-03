import math
 
x = int(input())
x_pow = round(math.pow(x, 1/5))
ok = 0
 
for a in range(-300,300):
  for b in range(-300,300):
    if a**5 - b**5 == x:
      print(a,b)
      ok = 1
      exit()