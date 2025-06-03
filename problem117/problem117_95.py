from collections import deque
N, M, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
da = deque()
i = 0
tmpK = 0
while tmpK <= K and i < N:
    tmpK += A[i]
    da.append(A[i])
    i += 1
# 一冊多い場合がある
if (tmpK > K):
    i -= 1
    tmpK -= da.pop()

# Bを増やしていく
db = deque()
j = 0
while tmpK <= K and j < M:
    tmpK += B[j]
    db.append(B[j])
    j += 1
# 一冊多い場合がある
if (tmpK > K):
    j -= 1
    tmpK -= db.pop()
tmptot = i+j
while len(da) > 0:
    tmpK -= da.pop()
    i -= 1
    while tmpK <= K and j < M:
        tmpK += B[j]
        db.append(B[j])
        j += 1
    # 一冊多い場合がある
    if (tmpK > K):
        j -= 1
        tmpK -= db.pop()
    if tmptot < i+j:
        tmptot = i+j
print(tmptot)