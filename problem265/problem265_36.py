import math
n=int(input())
num=math.ceil(n/1.08)
check=int(num*1.08)
if check==n:
    print(num)
else:
    print(':(')