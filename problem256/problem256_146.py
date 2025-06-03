import math

A,B = map(int,input().split())

#print(math.gcd(A,B))

C = A*B //(math.gcd(A,B))
print(C)
