import math

N = int(input())
A = []
for i in range(2,int(math.sqrt(N))+1):
    if N%i == 0:
        A.append(i + (N//i) - 2)
if not A:
    print(N-1)
else:
    print(min(A))