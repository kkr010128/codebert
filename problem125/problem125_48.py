from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
X=int(input())
from math import ceil
print(lcm(360,X)//X)