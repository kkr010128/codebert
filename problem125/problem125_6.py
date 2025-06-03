import math
X = int(input())
g = math.gcd(360, X)
l = X*360//g
print(l // X)
