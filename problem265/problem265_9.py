import math
n=int(input())
n1=math.floor(n/1.08)
n2=math.ceil(n/1.08)
if math.floor(n1*1.08)==n:
    print(n1)
elif math.floor(n2*1.08)==n:
    print(n2)
else:
    print(":(")