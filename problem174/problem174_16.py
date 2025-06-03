import math
K   = int(input())
Sum = 0
for A in range(1,K+1):
    for B in range(1,K+1):
        AB = math.gcd(A,B)
        if AB==1:
            Sum = Sum+K
        else:
            for C in range(1,K+1):
                Sum = Sum+math.gcd(AB,C)
print(Sum)