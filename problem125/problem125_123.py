import math
n=int(input())
a=360/n
b=a-360//n
print(int(n*360/math.gcd(n,360)/n))