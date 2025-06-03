from collections import defaultdict, Counter

n  = int(input())
lis = [input() for _ in range(n)]

a = Counter(lis)

tmp = 0
for key, value in a.items():
    tmp = max(value, tmp)

ans =[]
for k, v in a.items():
    if v == tmp:
        ans.append(k)

for i in sorted(ans):
    print(i)