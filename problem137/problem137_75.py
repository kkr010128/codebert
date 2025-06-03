from collections import defaultdict
from fractions import Fraction
N = int(input())
A = [0 for  _ in range(N)]
B = [0 for  _ in range(N)]
for i in range(N):
    A[i], B[i] = [int(i) for i in input().split()]
A.sort()
B.sort()

if N%2 == 1:
    target = ((N+1)//2)-1
    print(B[target]-A[target]+1)
else:
    target1 = ((N)//2)-1
    target2 = (N)//2
    num1 = (A[target1]+A[target2])/2
    num2 = (B[target1]+B[target2])/2
    print(int(((num2-num1)/0.5)+1))