from collections import Counter
MOD = 2019
S = input()[::-1]
X = [0]
for i in range(len(S)):
    X.append((X[-1]+int(S[i])*pow(10, i, MOD))%MOD)
C = Counter(X)
ans = 0
for v in C.values():
    ans += v*(v-1)//2
print(ans)