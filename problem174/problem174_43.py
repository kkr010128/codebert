r=range(1,int(input())+1)
from math import gcd 
print(sum(gcd(gcd(a,b),c) for a in r for b in r for c in r))