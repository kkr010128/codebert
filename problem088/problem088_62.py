N = int(input())
A_ = input().split()
A = [int(i) for i in A_]

S = 0
a = A[0]
for i in range(len(A)-1):
    if a > A[i+1]:
        S += a-A[i+1]
    else:
        a = A[i+1]
print(S)