import math

n = int(input())
sq = int(math.sqrt(n))

i=sq
for i in range(sq,0,-1):
    if n%i==0:
        j=n//i
        break
        
print(i+j-2)