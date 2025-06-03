from math import ceil

A, B, C, D = map(int, input().split())

E = ceil(C/B)
F = ceil(A/D)
print('Yes' if E <= F else 'No')
