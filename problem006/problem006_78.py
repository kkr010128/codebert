import math
n = input()
m = 100000
for i in range(n):
    m *= 1.05
    m = math.ceil(m/1000)*1000
print int(m)