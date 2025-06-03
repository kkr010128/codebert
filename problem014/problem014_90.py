import sys

lines = sys.stdin.readlines()

N = lines[0]
A = lines[1].strip().split(" ")

flag = 1

c = 0
i = 0
while flag == 1:
    flag = 0
    for j in reversed(range(i+1,len(A))):
        if int(A[j]) < int(A[j-1]):
            a = A[j]
            b = A[j-1]
            A[j] = b
            A[j-1] = a
            flag = 1
            c += 1
    i += 1

print " ".join(A)
print c