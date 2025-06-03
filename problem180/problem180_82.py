from sys import stdin
import math
from functools import reduce

n,k = [int(x) for x in stdin.readline().rstrip().split()]

m = n % k
print(min([m, k-m]))