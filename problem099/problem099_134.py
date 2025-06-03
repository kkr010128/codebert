import math
N, K = map(int,input().rstrip().split())
A = list(map(int,input().rstrip().split()))
maxX = max(A)
minX = 0
X = (maxX + minX)//2

while X!=minX:
    num = sum([math.ceil(A[i]/X)-1 for i in range(N)])
    if num<=K:
        maxX = X
    else:
        minX = X
    X = (maxX + minX)//2
num = sum([math.ceil(A[i]/maxX)-1 for i in range(N)])
if num<=K:
    print(maxX)
else:
    print(minX)