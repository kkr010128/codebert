from math import gcd

A,B = [int(i) for i in input().split()]

print(A*B//gcd(A,B))
