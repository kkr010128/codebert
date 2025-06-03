
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

try:
 while True:
  a, b = map(int, raw_input().split(' '))
  print gcd(a, b), lcm(a, b)
except EOFError:
  pass