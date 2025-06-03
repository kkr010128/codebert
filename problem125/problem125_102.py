from math import gcd

# X * K = 360 * n

lcm = lambda x, y: (x * y) // gcd(x, y)

X = int(input())
print(lcm(X, 360) // X)