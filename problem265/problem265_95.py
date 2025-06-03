from math import ceil
N = int(input())
X = ceil(N / 1.08)
if int(X * 1.08) == N:
    print(int(X))
else:
    print(':(')