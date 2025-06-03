import math
K   = int(input())
Sum = 0
for A in range(1,K+1):
    for B in range(1,K+1):
        for C in range(1,K+1):
            Sum = Sum+math.gcd(math.gcd(A,B),C)
print(Sum)