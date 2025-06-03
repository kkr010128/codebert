import sys

def to_i(e):
  return int(e)

def calc_gcd(a, b):
  if b > 0:
    return calc_gcd(b, a % b)
  else:
    return a

def calc_lcm(a, b):
  return ((a / calc_gcd(a, b)) * b)

while True:
  line = sys.stdin.readline()
  if not line: break
  a, b = map(to_i, line.rstrip().split(" "))
  gcd = calc_gcd(a, b)
  lcm = calc_lcm(a, b)
  print str(gcd) + " " + str(lcm)