D = int(input())
C = list(map(int, input().split()))
S = [None] * D
for i in range(D):
    S[i] = list(map(int, input().split()))
T = [None] * D
for i in range(D):
    T[i] = int(input())

lasts = [0] * 26
score = 0
for d in range(D):
    t = T[d]-1
    score += S[d][t]
    d += 1
    lasts[t] = d
    score -= sum(C[i] * (d-l) for i, l in enumerate(lasts))
    print(score)