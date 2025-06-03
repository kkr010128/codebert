#144_C
import math

n = int(input())
m = math.floor(math.sqrt(n))

div = 1
for i in range(1,m+1):
    if n % i == 0:
        div = i
        
print(int(div + n/div -2))