import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


D = int(readline())
CS = np.array(read().split(), np.int32)
C = CS[:26]
S = CS[26:].reshape((-1, 26))
del CS

last = np.zeros((26, ))


def compute_score(d, mask):
    score = -np.sum(C * (d + 1 - last) * mask)
    return score


ans = []
#SCORE = 0
for d in range(D):
    max_score = -10000000
    best_i = 0
    for i in range(26):
        mask = np.ones((26, ))
        mask[i] = 0
        score = compute_score(d, mask)
        score += S[d][i]

        if max_score < score:
            max_score = score
            best_i = i + 1

    ans.append(best_i)
    #SCORE += max_score
    #print(SCORE)

print('\n'.join(map(str, ans)))