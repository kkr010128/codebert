N, K = [int(i) for i in input().split()]
R, S, P = [int(i) for i in input().split()]
T = input()

def addScore(hand):
    if hand == 'r':
        return P
    elif hand == 's':
        return R
    else :
        return S

score = 0
score_flag = [0 for i in range(N)]

for l in range(len(T)):
    if l < K:
        score += addScore(T[l])
        score_flag[l] = 1
    else :
        if T[l] == T[l-K] and score_flag[l-K] == 1:
            continue
        else :
            score += addScore(T[l])
            score_flag[l] = 1
            
print(score)