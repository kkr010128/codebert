import math
n=int(input())

m=100000
k=100000
for i in range(n):
    m=1.05*k
    m=m/1000
    k=math.ceil(m)*1000
print(k)
    

