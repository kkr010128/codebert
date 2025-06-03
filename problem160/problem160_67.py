from itertools import combinations_with_replacement as comb_rplc

N, M, Q = list(map(int, input().split()))
A = []
B = []
C = []
D = []
for i in range(Q):
    in1, in2, in3, in4 = list(map(int,input().split()))
    A.append(in1 - 1)
    B.append(in2 - 1)
    C.append(in3)
    D.append(in4)
    
ans = 0
for seq in comb_rplc(range(1, M + 1), N):
    temp = 0
    for i in range(Q):
        if seq[B[i]] - seq[A[i]] == C[i]:
            temp += D[i]
        ans = max(ans, temp)
print(ans)