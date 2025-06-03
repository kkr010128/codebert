S = input()
from collections import defaultdict
d = defaultdict(int)
before = 0
for i in range(1,len(S)+1):
    now = (int(S[-i])*pow(10,i,2019)+before) % 2019
    d[now] += 1
    before = now
d[0] += 1
ans = 0
for i in d.values():
    ans += i*(i-1)//2
print(ans)