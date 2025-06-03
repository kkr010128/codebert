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
    mask = np.ones((26, ))
    mask[i] = 0
    score = S[d][i] - np.sum(C * (d + 1 - last) * mask)

    return score


def solve():
    output = []
    last = np.zeros((26, ))
    #SCORE = 0
    for d in range(D):
        max_score = float('-inf')
        best_i = 0
        for i in range(26):
            output.append(i)
            score = _compute_score(output, i, d, last)
            if max_score < score:
                max_score = score
                best_i = i + 1
            output.pop()
        output.append(best_i)
        last[best_i - 1] = d + 1
        #SCORE += max_score
        #print(SCORE)

    return output


if __name__ == "__main__":
    D, C, S = getInputs()
    ans = solve()
    print('\n'.join(map(str, ans)))