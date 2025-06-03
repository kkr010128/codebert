import sys

lines = sys.stdin.readlines()

N = lines[0]
A = lines[1].strip().split(" ")

print " ".join(A)

for i in range(1, len(A)):
    key = A[i]
    j = i - 1
    while j >= 0 and int(A[j]) > int(key):
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
    print " ".join(A)