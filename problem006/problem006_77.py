import math
a=int(input())
b=100000
for i in range(a):
    b=b*1.05
    b=b/1000
    b=math.ceil(b)
    b=b*1000
print(b)
