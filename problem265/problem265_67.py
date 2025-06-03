import math

n = int(input())
f = math.floor(n / 1.08)
c = math.ceil(n / 1.08)
for i in [f, c]:
    if math.floor(i*1.08) == n:
        print(i)
        exit()
print(':(')