import sys
def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x%y)

def lcm(x, y):
  return x * y //gcd(x,y)
    

for line in sys.stdin:
  x, y = map(int, line.split())
  print(gcd(x, y), lcm(x,y))