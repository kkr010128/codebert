
H, W, K = [int(n) for n in input().split(" ")]
M = []
for _ in range(H):
    a = [n for n in input()]
    assert(len(a) == W)
    M.append(a)

import copy
import itertools
"""
M = [[".", ".", "#"],
     ["#", "#", "#"]
]
W = len(M[0])
H = len(M)
K = 2
"""


def makeCombination(candidate, n, lessFlag):
    if len(candidate) <= 0:
        return [[]]
    _candidate = [n for n in candidate]
    _candidate = sorted(_candidate)
    result = []
    if lessFlag is False:
        tmp = list(set(list(itertools.combinations(_candidate, n))))
        for t in tmp:
            result.append(list(t))
    else:
        for i in range(n):
            result += makeCombination(candidate, i + 1, False)
        result += [[]]
    return result


def check(m, h, w):
    MM = copy.deepcopy(m)
    for a in h:
        for i in range(W):
            MM[a][i] = "R"
    for a in w:
        for i in range(H):
            MM[i][a] = "R"

    count = 0
    for i in range(len(MM)):
        for j in range(len(MM[i])):
            if MM[i][j] == "#":
                count += 1
    return count


HHH = makeCombination([n for n in range(H)], H, True)
WWW = makeCombination([n for n in range(W)], W, True)

OK = 0

for i in range(len(HHH)):
    for j in range(len(WWW)):
        if check(M, HHH[i], WWW[j]) == K:
            OK += 1
print(OK)

