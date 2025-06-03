N = int(input())
S = [input() for _ in range(N)]

res = {}
for s in S:
    if s in res:
        res[s] += 1
    else:
        res[s] = 1
max_ = max(res.values())

ans = []
for k in res:
    if res[k] == max_:
        ans.append(k)
ans.sort()

for a in ans:
    print(a)