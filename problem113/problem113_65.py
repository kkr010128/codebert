D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

import copy
MAX_SCORE = -float('inf')
MAX_ANS = -1
for K in range(26):
    v = 0
    ans = [0]*D
    L = [0]*26
    for i in range(1, D+1):
        max_score = -float('inf')
        max_idx = 0
        for j in range(26):
            temp = v
            temp += S[i-1][j]
            L_ = copy.copy(L)
            L_[j] = i
            for k in range(26):
                for l in range(i, min(i+K+1, D+1)):
                    temp -= C[k]*(l-L_[k])
            if temp >= max_score:
                max_score = temp
                max_idx = j
        v += S[i-1][max_idx]
        L[max_idx] = i
        for k in range(26):
            v -= C[k]*(i-L[k])
        ans[i-1] = max_idx+1
    if v >= MAX_SCORE:
        MAX_SCORE = v
        MAX_ANS = ans
print(*MAX_ANS, sep='\n')
