import math

def prime_check(x):
  if x == 2:
    return True
  limit = math.floor(math.sqrt(x)+1)
  cnt = 0
  for i in range(2,limit):
    if x%i == 0:
      cnt += 1
  if cnt == 0:
    return True
  else:
    return False
  
X = int(input())

while True:
  if prime_check(X):
    print(X)
    break
  else:
    X += 1