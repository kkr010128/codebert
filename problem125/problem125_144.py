from math import gcd
from sys import stdin
N = int(stdin.readline().rstrip())
print(360//gcd(N, 360))