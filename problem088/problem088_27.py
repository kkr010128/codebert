N = int(input())
A = list(map(int, input().split()))
SUM = 0;
for X in range(len(A)-1):
    if A[X] > A[X+1]:
        SUM += A[X]-A[X+1]
        A[X+1] = A[X]
print(SUM)
