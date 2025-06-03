#Scoring
import numpy as np
D = int(input())
C = np.array(list(map(int, input().split())))
S = np.zeros((D,26),int)
for i in range(D):
    S[i] = list(map(int, input().split()))

t = np.zeros(D,int)
for i in range(D):
    t[i] = int(input())

score = int(0)
ld = -np.ones(26,int)
tscore = np.zeros(26,int)
for i in range(D):
    cid = t[i]-1
    ld[cid] = i
    score -= np.sum(C*(i-ld))
    score += S[i,cid]
    print(score)
