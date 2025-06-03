import math

n = int(input())

x = n/1.08
t1 = math.ceil(x)
t2 = math.floor(x)

if math.floor(t1 * 1.08) == n:
    print(t1)
elif math.floor(t2*1.08) == n:
    print(t2)
else:
    print(':(')