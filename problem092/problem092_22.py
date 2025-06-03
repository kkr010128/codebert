import math
X, K, D = map(int,input().split())
X = math.fabs(X)
ans = 0
E = X//D
if E > K:
    ans = X - K * D
elif K%2 == E%2:
    ans = X-E*D
else:
    ans = -X+(E+1)*D
print(int(ans))