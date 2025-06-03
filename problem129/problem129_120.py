import math

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
maxA = A[len(A)-1]
valid = [True] * (maxA+1)

for i in range(len(A)):
    if valid[A[i]] == False:
        continue
    if i != 0 and A[i-1] == A[i]:
        valid[A[i]] = False
    else:
        for j in range(A[i]*2, maxA+1, A[i]):
            valid[j] = False

count = 0
for i in range(len(A)):
    if valid[A[i]] == True:
        count += 1
print(count)
