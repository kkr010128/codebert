x = int(input())
#import fractions
import math
from functools import reduce
def lcm_base(x, y):
  #return (x * y) // fractions.gcd(x, y)
  return (x * y) // math.gcd(x, y)

l = lcm_base(x, 360)
print(l//x)
