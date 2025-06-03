from collections import Counter

N, M = [int(_) for _ in input().split()]

wa = Counter()

ac = set()

for i in range(M):
    p, s = input().split()
    p = int(p)
    if p in ac: continue
    if s == 'WA':
        wa[p] += 1
    else:
        ac.add(p)
wa_cnt = 0
for v in ac:
    wa_cnt += wa[v]

print(len(ac), wa_cnt)
