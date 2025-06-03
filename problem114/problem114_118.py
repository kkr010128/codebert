d = int(input())
C = list(map(int, input().split()))
S = []
for _ in range(d):
    S.append(list(map(int, input().split())))
v = 0
LDs = [0 for _ in range(26)]
for i in range(d):
    t = int(input()) - 1
    R = [(i + 1 - LDs[j]) * C[j] for j in range(26)]
    del R[t]
    v += S[i][t] - sum(R)
    LDs[t] = i + 1
    print(v)