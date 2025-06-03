import numpy as np
import math
import collections

N = int(input())
A = list(map(int, input().split()))


ans = 0
node_num = 1
pre_node_num = 1
B = [1 - A[0]]
ruisekiA = [0 for i in range(N + 2)]
ruisekiA[N] = A[N]
ruisekiA[N + 1] = 0
for i in range(N - 1, -1, -1):
    ruisekiA[i] = ruisekiA[i + 1] + A[i]


for i in range(1, N + 1):
    tmpB = min(2 * B[i - 1] - A[i], ruisekiA[i + 1])
    #print(tmpB, B[i - 1] - A[i])
    if (tmpB < 0) or (tmpB < B[i - 1] - A[i]):
        ans = -1
        break
    if i == N:
        tmpB = 0
    B.append(tmpB)

if N == 0 and A[0] != 1:
    ans = -1

if ans != -1:
    ans = sum(A) + sum(B)
print(ans)
