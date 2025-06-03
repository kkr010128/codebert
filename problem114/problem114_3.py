import numpy as np


D = int(input())
c = np.array(list( map(int,input().split())))
S = np.zeros((D,26))
for i in range(D):
    S[i] = np.array(list( map(int,input().split())))

T = np.array([])
for i in range(D):
    T = np.append(T,int(input()))

"""
D = 365
c = np.random.randint(0,100,size=(26))
S = np.random.randint(0,20000,size=(D,26))
"""

def calc_score(T,D,c,S):
    last = np.ones(26) * (-1)
    scores = []
    score = 0
    for d in range(D):
        i = int(T[d])-1
        score += S[d,i]
        last[i] = d
        score -= np.sum(c*(d-last))
        scores.append(score)
    score = max([10**6+score,0])
    return score,scores

_,ans = calc_score(T,D,c,S)
for a in ans:
    print(int(a))