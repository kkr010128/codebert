import math
 
X = int(input())
ans = 0
 
while ans == 0:
  factor = 0
  if X % 2 == 0 and X != 2:
    X +=1
    continue      
  for divisor in range(2, X // 2):
    if X % divisor == 0:
      factor += 1          
  if factor == 0:
    ans =X
  X +=1    
    
print(ans) 