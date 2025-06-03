from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cA = Counter(A)

allS = 0
for key in cA:
    allS += cA[key] * (cA[key] - 1) / 2

for i in range(N):
    if A[i] in cA.keys():
        print(int(allS - (cA[A[i]] - 1)))
    else:
        print(int(allS))