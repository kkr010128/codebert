def lcm(x, y):
  import math
  return (x * y) // math.gcd(x, y)

def main():
  A, B = map(int, input().split())
  ans = lcm(A, B)
  print(ans)
main()