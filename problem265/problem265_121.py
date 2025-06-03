import math
n = float(input())
m = n / 1.08
if math.floor(math.floor(m) * 1.08) == n:
    print(math.floor(m))
elif math.floor(math.ceil(m) * 1.08) == n:
    print(math.ceil(m))
else:
    print(':(')