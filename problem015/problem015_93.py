import sys

lines = sys.stdin.readlines()

N = lines[0]
A = lines[1].strip().split(" ")

count = 0
for i in range(len(A)):
    minj = i
    for j in range(i, len(A)):
        if int(A[j]) < int(A[minj]):
            minj = j
    if i != minj:
        a = A[i]
        b = A[minj]
        A[i] = b
        A[minj] = a
        count += 1

print " ".join(A)
print count