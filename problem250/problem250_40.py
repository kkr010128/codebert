X = int(input())

def is_Prime(x):
  for i in range(2, x+1):
    if i * i + 1 > x:
      return True
    if x % i == 0:
      return False

for i in range(X, 2*X+1):
  if is_Prime(i):
    print(i)
    break
