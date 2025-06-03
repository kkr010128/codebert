N = int(input())
A = [ x for x in input().split(" ")]
orig_A = A[:]

#bubblesort
for i in range(0, N):
    for j in range(N-1, i, -1):
        if int(A[j][1]) < int(A[j-1][1]):
            A[j], A[j-1] = A[j-1], A[j]

print(*A)
print("Stable")


#selectionsort
for i in range(0, N):
    minj = i
    for j in range(i, N):
        if int(orig_A[j][1]) < int(orig_A[minj][1]):
            minj = j
    orig_A[i], orig_A[minj] = orig_A[minj], orig_A[i]


print(*orig_A)
print("Stable" if A == orig_A else "Not stable")