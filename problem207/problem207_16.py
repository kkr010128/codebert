import numpy as np

A = []
for i in range(3):
  b = list(map(int, input().split()))
  A.append(b)

N = int(input())

NP_A = np.array(A)
b = []
for n in range(N):
  b.append(int(input()))

for n in range(N):
  NP_A = np.where(NP_A==b[n], 0, NP_A)

ans = "No"

for i in range(2):
    if 0 in NP_A.sum(axis=i):
        ans = "Yes"
        break

if ans == "Yes":
    pass
else:
    sum = 0
    for i in range(3):
        sum += NP_A[i, i]
    if sum == 0:
        ans = "Yes"
    else:
        sum = NP_A[0, 2] + NP_A[1, 1] + NP_A[2, 0]
        if sum == 0:
            ans = "Yes"

print(ans)