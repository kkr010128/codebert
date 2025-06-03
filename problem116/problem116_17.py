A = str(input())
B = str(input())
c = 0
lenA = len(A)
for i in range(lenA):
    if A[i] != B[i]:
        c += 1
print(c)
