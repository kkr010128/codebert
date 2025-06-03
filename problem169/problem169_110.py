from sys import stdin
import sys, math

n = int(stdin.readline().rstrip())

a = [0 for i in range(n)]
d = [int(x) for x in stdin.readline().rstrip().split()]

for i in range(n-1):
    k = d[i]
    a[k-1] = a[k-1] + 1

for i in range(n):
    print(a[i])