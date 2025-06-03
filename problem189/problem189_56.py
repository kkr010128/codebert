import math
def count(n, r):
    return math.factorial(n) // math.factorial(n - r)
def main():
  N, M = map(int, input().split())
  if (N == 0 and M == 0) or (N == 1 and M == 1):
    ans = 0
  elif N == 0 or N == 1:
    y = count(M, 2)
    ans = y
  elif M == 0 or M == 1:
    x = count(N, 2)
    ans = x
  else:
    x = count(N, 2)
    y = count(M, 2)
    ans = x + y
  print(int(ans/2))

main()

