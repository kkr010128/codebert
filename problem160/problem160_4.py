import itertools

N,M,Q=map(int,input().split())

A=[]
for i in range(Q):
    A.append(list(map(int,input().split())))
    A[i][0] -= 1
    A[i][1] -= 1

score = 0
max = 0

for iter in itertools.combinations_with_replacement(range(1,M+1),N):

    score = 0
    for i in range(Q):
        if iter[A[i][1]] - iter[A[i][0]] == A[i][2]:
            score += A[i][3]

    if max < score:
        max = score


print(max)