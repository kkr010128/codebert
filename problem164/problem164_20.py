from math import ceil
A, B, C, D = map(int, input().split())
time_A, time_C = ceil(A/D), ceil(C/B)
print('Yes') if time_A >= time_C else print('No')