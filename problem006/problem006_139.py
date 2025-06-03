import math
m=10**2
for i in range(input()):
    m*=1.05
    m=math.ceil(m)
print int(m*(10**3))