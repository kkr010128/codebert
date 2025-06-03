import math

p = 100
for i in range(int(input())):
    p = math.ceil(p * 1.05)
print(p * 1000)