import math
def isprime(x):
 if x == 2:
  return True
 elif x < 2 or x % 2 == 0:
  return False
 else:
  for i in range(3, int(math.sqrt(x)) + 1,2):
   if x % i == 0:
    return False 
  return True

n = int(input())
cnt = 0
for i in range(n):
 x = int(input())
 if isprime(x):
  cnt += 1
print(str(cnt))