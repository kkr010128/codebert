from sys import stdin
import math

n, m = [int(x) for x in stdin.readline().rstrip().split()]

if n * 500 >= m:
    print('Yes')
else:
    print('No')