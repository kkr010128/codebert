import math
n=int(input())
r1=math.ceil(n/1.08)
r2=(n+1)/1.08
if r1<r2:
    print(r1)
else:
    print(":(")
