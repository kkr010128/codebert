import math

N = int(input())
x = math.floor(N / 1.08)
y = math.ceil(N / 1.08)

if int(x*1.08) == N:
    print(x)
elif int(y*1.08) == N:
    print(y)
else:
    print(':(')