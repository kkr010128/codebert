import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

from numba import njit


def getInputs():
    D = int(readline())
    CS = np.array(read().split(), np.int32)
    C = CS[:26]
    S = CS[26:].reshape((-1, 26))
    return D, C, S


def _compute_score(output, i, d, last):
    mask = np.ones((26, ), np.int32)
    mask[i] = 0
    score = S[d][i] - np.sum(C * (d + 1 - last) * mask)

    return score


def _evaluate(output, i, d, last, k):
    score = _compute_score(output, i, d, last)
    score -= np.sum(C * (d + k + 1 - last))
    return score


def solve(k):
    output = np.array([], np.int32)
    last = np.zeros((26, ), np.int32)
    SCORE = 0
    for d in range(D):
        max_score = float('-inf')
        best_i = 0
        for i in range(26):
            output = np.append(output, i)
            #score = _compute_score(output, i, d, last)
            score = _evaluate(output, i, d, last, k)
            if max_score < score:
                max_score = score
                best_i = i + 1
            output = output[:-1]
        output = np.append(output, best_i)
        last[best_i - 1] = d + 1
        SCORE += max_score

    return output, SCORE


D, C, S = getInputs()

max_score = float('-inf')
for k in range(7, 14):
    ans, score = solve(k)
    if max_score < score:
        max_score = score
        ANS = ans

print('\n'.join(ANS.astype(str).tolist()))