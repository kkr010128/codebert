A, B = map(int,input().split())

import math

c = math.gcd(A,B)

d = (A*B) / c 

print(int(d))