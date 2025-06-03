import math
N = int(input())
A = [0]*(N)
for i in range(0,N):
    A[i] = math.floor((N-1)/(i+1))
print(sum(A))