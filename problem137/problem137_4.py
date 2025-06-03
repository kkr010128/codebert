#
import sys
import math
import numpy as np
import itertools

n = int(input())

# n行の複数列ある数値をそれぞれの配列へ
a, b = [0]*n, [0]*n
for i in range(n): a[i], b[i] = map(int, input().split())

#print(a,b)

a.sort()
b.sort()

if n % 2 == 0:
    t = a[n//2-1] + a[n//2]
    s = b[n//2-1] + b[n//2]
    print(s-t+1)
else:
    t = a[n//2]
    s = b[n//2]
    print(s-t+1)


