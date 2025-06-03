import numpy as np
N = int(input())
S = [[] for I in range(0,N)]
for T in range(0,N):
    A = int(input())
    S[T] = np.zeros((A,2),dtype=int)
    for TT in range(0,A):
        S[T][TT,:] = np.array([int(X) for X in input().split()])
    
MAX = 0
for P in range(pow(2,N)-1,-1,-1):
    Bin    = [int(X) for X in list(('{:0'+str(N)+'b}').format(P,'b'))]
    BIndex = [I for I,N in enumerate(Bin) if N==1]
    Flag   = True
    for PT in BIndex:
        for PTB in range(0,S[PT].shape[0]):
            if S[PT][PTB,1]==0 and (S[PT][PTB,0]-1) in BIndex:
                Flag = False
                break
            if S[PT][PTB,1]==1 and (S[PT][PTB,0]-1) not in BIndex:
                Flag = False
                break
        if not Flag:
            break
    if Flag:
        MAX = len(BIndex)
        break
print(MAX)