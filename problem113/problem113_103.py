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


@njit('(i8, i4[:], i4[:, :], i4[:], )', cache=True)
def _compute_score1(D, C, S, out):
    score = 0
    last = np.zeros(26, np.int32)
    for d in range(len(out)):
        i = out[d]
        score += S[d, i]
        last[i] = d + 1
        score -= np.sum(C * (d + 1 - last))
    return last, score


def step1(D, C, S):
    #out = np.zeros(D, np.int32)
    out = []
    LAST = 0
    for d in range(D):
        max_score = -10000000
        best_i = 0
        
        for i in range(26):
            #out[d] = i
            out.append(i)
            last, score = _compute_score1(D, C, S, np.array(out, np.int32))
            if max_score < score:
                max_score = score
                LAST = last
                best_i = i
            out.pop()

        #out[d] = best_i
        out.append(best_i)

    return np.array(out), LAST, max_score


def output(out):
    out += 1
    print('\n'.join(out.astype(str).tolist()))


D, C, S = getInputs()
out, _, score = step1(D, C, S)
output(out)