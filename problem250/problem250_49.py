X = int(input())
def Sosuu_not(n):
  for p in range(2, n):
    if n % p == 0:
        return False
  else:
    return True
while True:
  if Sosuu_not(X) == True:
    print(X)
    break
  X += 1