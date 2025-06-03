from math import floor
from sys import stdin
A, B, N = [int(_) for _ in stdin.readline().rstrip().split()]
def solve(x):
    return floor(A*x/B)-A*floor(x/B)
print(solve(min(B-1, N)))