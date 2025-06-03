import math
A, B = map(int,input().split())
LA = []
LB = []

X = math.ceil(A / 0.08)
Y = math.ceil(B / 0.1)
N = int((A+1) // 0.08)
M = int((B+1) // 0.1)

for i in range(X, N+1):
    LA.append(i)
for i in range(Y, M+1):
    LB.append(i)

ans = set(LA) & set(LB)
ans_list = list(ans)
if not ans_list:
    print(-1)
else:
    print(min(ans_list))