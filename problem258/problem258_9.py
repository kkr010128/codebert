import math

n = int(input())
ans = 0
if n== 0:
  print(0)
  exit()


if n%2 == 1:
  print(0)
else:
  for j in range(1,100):
    if n//((5**j)*2) == 0:
      break
    ans += n//((5**j)*2)
    
    
  print(ans)