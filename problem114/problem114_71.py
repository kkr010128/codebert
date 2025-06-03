import numpy as np
D = int(input())
C = list(map(int, input().split()))
B = np.array([0] * 26)
S = [list(map(int, input().split())) for _ in range(D)]
satisfaction = 0
for d in range(1, D+1):
    t = int(input())
    B[t-1] = d
    deduction = sum(C * (d - B))
    satisfaction += S[d-1][t-1] - deduction
    print(satisfaction)