from collections import Counter
n = int(input())
a1, a2 = [], []
for idx, ai in enumerate(map(int, input().split())):
    a1.append(ai+idx)
    a2.append(idx-ai)
cnt = Counter(a2)
res = 0
for idx, i in enumerate(a1):
    cnt[a2[idx]] -= 1
    res += cnt[i]
print(res)