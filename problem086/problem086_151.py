
from sys import stdin
from math import ceil

N,X,T = [int(x) for x in stdin.readline().rstrip().split()]

result = ceil( N / X ) * T

print(result)