import math

def main():
  X = int(input())

  if X == 2: return 2
  if X == 3: return 3
  if X == 4 or X == 5: return 5
  if X == 6 or X == 7: return 7
  if X == 8: return 11

  while True:
    if X % 2 != 0:
      for i in range(3, int(math.sqrt(X))+1, 2):
        if X % i == 0: break
      else: return X
    X += 1

ans = main()
print(ans)