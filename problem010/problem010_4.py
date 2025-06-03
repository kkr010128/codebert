N = int(input())
A = (input()).split()
for i in range(0,N):
    A[i] = int(A[i])
for i in range(0,N):
    innum = A[i]
    j = i - 1
    while j>=0 and innum < A[j]:
        A[j+1] = A[j]
        j = j -1
    A[j+1] = innum
    for j in range(0,N):
        if j < N-1:
            print(A[j], end=" ")
        else:
            print(A[j])