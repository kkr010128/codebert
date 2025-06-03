import math

n = int(input())
m = 100000.0
for i in range(n):
    m = math.ceil((m * 1.05)/1000)*1000

print(int(m))
