N=int(input())
import math
X=math.ceil(N/1.08)
if int(X*1.08)==N:
    print(X)
else:
    print(':(')