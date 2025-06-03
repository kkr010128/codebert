from collections import Counter

n = int(input())

s = [input() for _ in range(n)]

c = Counter(s)

csort = sorted(c.items(), key=lambda x:x[1],reverse=True)

maxc = csort[0][1]
ans = []
for s,v in csort:
    if v == maxc:
        ans.append(s)
        
anssort = sorted(ans)

for s in anssort:
    print(s)