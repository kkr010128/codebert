def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

import math
A,B=map(int,input().split())

print(A*B//gcd(A,B))