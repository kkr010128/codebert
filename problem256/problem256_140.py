import math

m,n = map(int,input().split())

print(m*n//(math.gcd(m, n)))
