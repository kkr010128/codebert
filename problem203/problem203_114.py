from math import ceil

A, B = map(int, input().split())

max_A = (A+1)*12.5
min_A = (A)*12.5
max_B = (B+1)*10.0
min_B = B*10.0

if min_A < max_B and min_A >= min_B:
    print(ceil(min_A))
elif min_B < max_A and min_B >= min_A:
    print(ceil(min_B))
else:
    print(-1)
