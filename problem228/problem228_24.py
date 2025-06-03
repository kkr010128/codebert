import math

h = int(input())
n = int(math.log2(h))
 
a = 2
r = 2
S = (a*(r**n)-a) // (r-1)
print(S + 1)