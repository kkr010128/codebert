import math

N,M,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.append(math.inf)
B.append(math.inf)

best = 0
i = j = 0

while K >= A[i]:
    K -= A[i]
    i += 1

while True:
    while K >= B[j]:
        K -= B[j]
        j += 1

    best = max(best, i+j)

    if i == 0: break

    i -= 1
    K += A[i]

print(best)
