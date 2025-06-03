import math
n = int(input())
print(360*n//math.gcd(360,n)//n)