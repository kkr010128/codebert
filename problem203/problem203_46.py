import math
a, b = list(map(int, input().split()))
for i in range(1, 1250):
    p8 = math.floor(i * 0.08)
    p10 = math.floor(i * 0.10)
    if p8 == a and p10 == b:
        print(i)
        exit()
print(-1)