ma = lambda :map(int,input().split())
ni = lambda:int(input())
import collections
import math
import itertools
import fractions
gcd = fractions.gcd
a,b = ma()
print(a*b//gcd(a,b))
