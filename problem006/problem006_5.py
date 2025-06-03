import math
n=input()
m=10**2
for i in range(n):
    m=m*1.05
    m=math.ceil(m)
print int(m*(10**3))