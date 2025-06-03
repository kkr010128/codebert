n=int(input())
import math
move_min=1+n-2
for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
        move_min=min(move_min,i+n//i-2)
print(move_min)