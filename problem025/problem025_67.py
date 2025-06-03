N = int(input())
A = list(map(int,input().split()))
M = int(input())
Q = list(map(int,input().split()))
SL = []
for bit in range(1<<N):
    SUM = 0
    for i in range(N):
        if bit & (1<<i):
            SUM += A[i]
    SL.append(SUM)
for q in Q:
    if q in SL:
        print('yes')
    else:
        print('no')
