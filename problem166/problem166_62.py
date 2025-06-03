import collections
import sys
S = input()[::-1]
    
MOD=2019
X = [0]
for i, s in enumerate(S):
    X.append((X[-1]+int(s)*pow(10,i,MOD))%MOD)
    
c = collections.Counter(X)
ans = 0
for v in c.values():
    ans += v * (v - 1) // 2
print(ans)