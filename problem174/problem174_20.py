import math
a = int(input())
b = 0
for i in range(1,a+1):
    for j in range(1,a+1):
        for k in range(1,a+1):
         b+=math.gcd(math.gcd(i,j),k)
print(b)