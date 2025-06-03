from collections import defaultdict
import math
def P(n, r):
    return math.factorial(n)//math.factorial(n-r)
def C(n, r):
    return P(n, r)//math.factorial(r)
S = input()[::-1]
N = len(S)
cnt = [0]*N
tmp = 0
d = defaultdict(int)
d[0] += 1
for i in range(N):
    tmp += int(S[i])*pow(10,i,2019)
    tmp %= 2019
    d[tmp] += 1
ans = 0
for v in d.values():
    if v >= 2:
        ans += C(v,2)
print(ans)