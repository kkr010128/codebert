N = int(input())
A = [int(x) for x in input().split()]
Sum = 0
Dff = 0

for i in range(N-1):
    Dff = A[i] - A[i+1]
    if Dff > 0:
        A[i+1] += Dff
        Sum += Dff
    Dff = 0

print(Sum)