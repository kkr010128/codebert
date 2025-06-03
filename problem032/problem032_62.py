import math

input()
xl = [int(s) for s in input().split()]
yl = [int(s) for s in input().split()]

m1 = 0
m2 = 0
m3 = 0
m4 = 0
for x, y in zip(xl, yl):
    fabs = math.fabs(x - y) 
    m1 += fabs
    m2 += fabs ** 2
    m3 += fabs ** 3
    m4 = max(fabs, m4)
    
print(m1)
print(math.pow(m2, 1/2))
print(math.pow(m3, 1/3))
print(m4)