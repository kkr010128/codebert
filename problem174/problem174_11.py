import math
k=int(input())

result=0
for i in range(1,k+1):
    for j in range(1,k+1):
        first=math.gcd(i,j)
        for g in range(1,k+1):
            result=result+math.gcd(first,g)
print(result)
