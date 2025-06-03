import math
a=100
n=int(input())
for i in range(n):
    a=a*1.05
    a=math.ceil(a)
print(a*1000)
