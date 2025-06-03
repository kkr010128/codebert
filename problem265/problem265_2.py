import math
a = input()
N = int(a)

X = N//1.08 + 1
x = math.floor(X*1.08)
if x == N:
    print(int(X))
else:
    print(':(')