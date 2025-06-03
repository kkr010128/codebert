import math
n = float(input())
a = math.floor(n/1.08)
x = []
if math.floor((a)*1.08) == n:
  print(a)
elif math.floor((a+1)*1.08) == n:
  print(a+1)
elif math.floor((a+2)*1.08) == n:
  print(a+2)
elif math.floor((a+3)*1.08) == n:
  print(a+3)
elif math.floor((a-1)*1.08) == n:
  print(a-1)
else:
  print(":(")