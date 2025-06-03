N = int(input())
A = [int(i) for i in input().split()]

possess = 1000

for i in range(N-1):
    if A[i] < A[i+1]:
        stock = possess//A[i]
        possess = possess % A[i] + A[i+1] * stock


print(possess)